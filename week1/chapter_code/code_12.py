import json
from pathlib import Path

def save_json(data: dict,path: Path) -> None:
	text = json.dumps(data,ensure_ascii=False,
			indent=2,allow_nan=False)
	path.parent.mkdir(parents=True,exist_ok=True)
	with path.open("w",encoding="utf-8") as handle:
		handle.write(text + "\n")

def read_json(path:Path) -> dict:
	with path.open("r",encoding="utf-8") as handle:
		return json.load(handle)

source = {"cpu_percent":25.5,"note":"首次采集"}
target=Path("reports/first.json")
save_json(source,target)
assert read_json(target) == source

print(read_json(target))
print("保存和读取验证成功")
