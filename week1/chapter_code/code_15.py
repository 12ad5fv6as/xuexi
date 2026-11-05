from  pathlib import Path

try:
	content = Path("scratch/config.txt").read_text(encoding="utf_8")
except FileNotFoundError:
	print("congfig missing;use classroom default")
else:
	print("read succeeded:",content)
finally:
	print("this attempt has ended")
