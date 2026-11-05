from pathlib import Path

path = Path("scratch/utf8.txt")
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("w", encoding="utf-8") as handle:
    handle.write("系统采集正常\n")
with path.open("r", encoding="utf-8") as handle:
    print(handle.read())
