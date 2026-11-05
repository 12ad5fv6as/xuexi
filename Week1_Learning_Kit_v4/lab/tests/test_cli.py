import json
import pytest
from monitor import __main__ as cli


@pytest.fixture
def fake_collect(monkeypatch):
    def collect(self):
        return {"metrics": {"cpu_percent": 20, "memory_percent": 30,
                            "disk_percent": 40},
                "process_collection": {"skipped_count": 0}}
    monkeypatch.setattr(cli.SystemCollector, "collect", collect)


def arguments(tmp_path):
    return ["--output", str(tmp_path / "report.json"),
            "--log-file", str(tmp_path / "monitor.log")]


def test_success(tmp_path, fake_collect, capsys):
    assert cli.main(arguments(tmp_path)) == 0
    assert json.loads((tmp_path / "report.json").read_text())["metrics"]
    assert "Report:" in capsys.readouterr().out
    assert "report saved" in (tmp_path / "monitor.log").read_text()


def test_invalid_interval(tmp_path, capsys):
    assert cli.main(arguments(tmp_path) + ["--interval", "0"]) == 1
    assert "ValueError" in capsys.readouterr().err
    assert not (tmp_path / "report.json").exists()


def test_output_parent_is_file(tmp_path, fake_collect, capsys):
    blocker = tmp_path / "blocker"
    blocker.write_text("file")
    args = ["--output", str(blocker / "report.json"),
            "--log-file", str(tmp_path / "monitor.log")]
    assert cli.main(args) == 1
    assert "Sampling failed" in capsys.readouterr().err


def test_log_parent_is_file(tmp_path, capsys):
    blocker = tmp_path / "blocker"
    blocker.write_text("file")
    args = ["--output", str(tmp_path / "report.json"),
            "--log-file", str(blocker / "monitor.log")]
    assert cli.main(args) == 1
    assert "Sampling failed" in capsys.readouterr().err
    assert not (tmp_path / "report.json").exists()


def test_same_output_and_log(tmp_path, capsys):
    path = str(tmp_path / "same.json")
    assert cli.main(["--output", path, "--log-file", path]) == 1
    assert "must be different" in capsys.readouterr().err


def test_parser_rejects_bad_type(tmp_path):
    with pytest.raises(SystemExit) as exc:
        cli.main(arguments(tmp_path) + ["--top", "five"])
    assert exc.value.code == 2


def test_repeat_does_not_duplicate_logs(tmp_path, fake_collect):
    assert cli.main(arguments(tmp_path)) == 0
    assert cli.main(arguments(tmp_path)) == 0
    text = (tmp_path / "monitor.log").read_text()
    assert text.count("report saved") == 2
    assert not cli.logger.handlers
