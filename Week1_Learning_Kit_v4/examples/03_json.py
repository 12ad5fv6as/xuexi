"""Writes only to scratch/ under the CURRENT working directory."""
import json
from pathlib import Path

path = Path("scratch/example_report.json")
path.parent.mkdir(parents=True, exist_ok=True)
source = {"cpu": 25.5, "ok": True, "gpu": None, "note": "示例"}
with path.open("w", encoding="utf-8") as handle:
    json.dump(source, handle, ensure_ascii=False, allow_nan=False)
with path.open("r", encoding="utf-8") as handle:
    restored = json.load(handle)
assert restored == source
print(path.resolve())
