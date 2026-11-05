from pathlib import Path

try:
    content = Path("scratch/config.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("config missing; use classroom default")
else:
    print("read succeeded:", content)
finally:
    print("this attempt has ended")
