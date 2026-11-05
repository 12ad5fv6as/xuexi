from monitor.storage import read_json,save_json

def test_json_round_trip(tmp_path):
        path = tmp_path / "nested" / "report.json"
        data = {"ok": True,"description":"测试"}
        save_json(data,path)
        assert path.is_file()
        assert read_json(path) == data
