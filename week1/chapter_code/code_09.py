from pathlib import Path
path = Path("reports/first.json")
print(Path.cwd())
print(path.resolve())
path.parent.mkdir(parents=True,exist_ok=True)
