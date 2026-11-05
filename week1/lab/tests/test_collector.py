from types import SimpleNamespace
import pytest
from monitor import collector as module
from monitor.collector import SystemCollector


@pytest.mark.parametrize("interval", [0, -1, 11, float("nan"),
                                     float("inf"), True])
def test_invalid_interval(interval):
    with pytest.raises(ValueError):
        SystemCollector(interval=interval)


@pytest.mark.parametrize("top", [0, 101, 2.5, True])
def test_invalid_top(top):
    with pytest.raises(ValueError):
        SystemCollector(top=top)


class FakeProcess:
    def __init__(self, pid, rss, denied=False):
        self.pid, self.rss, self.denied = pid, rss, denied

    def memory_info(self):
        if self.denied:
            raise module.psutil.AccessDenied(self.pid)
        return SimpleNamespace(rss=self.rss)

    def name(self):
        return f"fake-{self.pid}"


def test_order_and_partial_failure(monkeypatch):
    processes = [FakeProcess(1, 20), FakeProcess(2, 50),
                 FakeProcess(3, 30), FakeProcess(4, 0, denied=True)]
    monkeypatch.setattr(module.psutil, "process_iter", lambda: iter(processes))
    rows, skipped = SystemCollector(top=2)._top_processes()
    assert [row["pid"] for row in rows] == [2, 3]
    assert skipped == 1


def test_process_disappears(monkeypatch):
    class Gone(FakeProcess):
        def name(self):
            raise module.psutil.NoSuchProcess(self.pid)
    monkeypatch.setattr(module.psutil, "process_iter",
                        lambda: iter([Gone(8, 100), FakeProcess(9, 50)]))
    rows, skipped = SystemCollector()._top_processes()
    assert [row["pid"] for row in rows] == [9]
    assert skipped == 1


def test_deterministic_snapshot(monkeypatch):
    monkeypatch.setattr(module.psutil, "cpu_percent", lambda interval: 80.0)
    memory = SimpleNamespace(percent=50.0, total=1024**3, available=512*1024**2)
    disk = SimpleNamespace(percent=25.0, total=4*1024**3)
    monkeypatch.setattr(module.psutil, "virtual_memory", lambda: memory)
    monkeypatch.setattr(module.psutil, "disk_usage", lambda path: disk)
    monkeypatch.setattr(module.psutil, "cpu_count", lambda logical: 4)
    monkeypatch.setattr(module.psutil, "process_iter", lambda: iter([]))
    result = SystemCollector().collect()
    assert result["metrics"]["cpu_state"] == "high"
    assert result["metrics"]["memory_total_mib"] == 1024.0
    assert result["metrics"]["disk_total_gib"] == 4.0
    assert result["process_collection"]["incomplete"] is False
    assert result["sample_started_utc"] <= result["timestamp_utc"]
