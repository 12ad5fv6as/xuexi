import json
import pytest
from monitor.storage import read_json, save_json


def test_round_trip(tmp_path):
    data = {"note": "\u6d4b\u8bd5", "values": [1, True, None]}
    path = tmp_path / "nested" / "report.json"
    save_json(data, path)
    assert path.is_file()
    assert read_json(path) == data


def test_invalid_data_preserves_old_file(tmp_path):
    path = tmp_path / "report.json"
    save_json({"value": 10}, path)
    with pytest.raises(ValueError):
        save_json({"value": float("nan")}, path)
    assert read_json(path) == {"value": 10}


def test_blocked_parent(tmp_path):
    blocker = tmp_path / "blocker"
    blocker.write_text("not a directory", encoding="utf-8")
    with pytest.raises(OSError):
        save_json({"ok": True}, blocker / "report.json")


def test_invalid_json(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{bad}", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        read_json(path)


def test_non_object_report(tmp_path):
    path = tmp_path / "array.json"
    path.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        read_json(path)
