from monitor import collector as module

def test_fixed_cpu_reading(monkeypatch):
    monkeypatch.setattr(
        module.psutil, "cpu_percent",
        lambda interval: 25.0,
    )
    assert module.psutil.cpu_percent(interval=0.1) == 25.0
