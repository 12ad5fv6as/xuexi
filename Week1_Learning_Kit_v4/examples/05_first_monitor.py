"""Day 2 minimum version, BEFORE the error handling lessons."""
import json
from datetime import datetime, timezone
from pathlib import Path
import psutil

cpu = psutil.cpu_percent(interval=0.5)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
report = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
          "cpu_percent": cpu, "memory_percent": memory.percent,
          "disk_percent": disk.percent}
path = Path("reports/first_report.json")
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("w", encoding="utf-8") as handle:
    json.dump(report, handle, indent=2, allow_nan=False)
print(path.resolve())
