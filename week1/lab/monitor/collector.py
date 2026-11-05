"""Collect one sequential snapshot from the current OS-visible environment."""
import logging
import math
import platform
from datetime import datetime, timezone
from typing import Any

import psutil
from monitor.rules import classify_usage, validate_percentage

logger = logging.getLogger("monitor.collector")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class SystemCollector:
    def __init__(self, disk_path: str = "/", interval: float = 0.5,
                 top: int = 5, cpu_threshold: float = 80.0) -> None:
        if (isinstance(interval, bool)
                or not isinstance(interval, (int, float))
                or not math.isfinite(interval)
                or not 0 < interval <= 10):
            raise ValueError("interval must be finite, > 0 and <= 10 seconds")
        if isinstance(top, bool) or not isinstance(top, int) or not 1 <= top <= 100:
            raise ValueError("top must be an integer between 1 and 100")
        validate_percentage(cpu_threshold, "cpu_threshold")
        self.disk_path = disk_path
        self.interval = float(interval)
        self.top = top
        self.cpu_threshold = float(cpu_threshold)

    def collect(self) -> dict[str, Any]:
        started = utc_now()
        cpu = psutil.cpu_percent(interval=self.interval)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage(self.disk_path)
        processes, skipped = self._top_processes()
        return {
            "schema_version": 1,
            "sample_started_utc": started,
            "timestamp_utc": utc_now(),
            "host": {
                "os": platform.system(),
                "architecture": platform.machine(),
                "logical_cpu_count": psutil.cpu_count(logical=True),
            },
            "sampling": {"cpu_interval_seconds": self.interval},
            "metrics": {
                "cpu_percent": round(cpu, 2),
                "cpu_state": classify_usage(cpu, self.cpu_threshold),
                "cpu_threshold": self.cpu_threshold,
                "memory_percent": round(memory.percent, 2),
                "memory_total_mib": round(memory.total / 1024**2, 2),
                "memory_available_mib": round(memory.available / 1024**2, 2),
                "disk_percent": round(disk.percent, 2),
                "disk_total_gib": round(disk.total / 1024**3, 2),
                "disk_path": self.disk_path,
            },
            "top_processes_by_rss": processes,
            "process_collection": {
                "skipped_count": skipped,
                "incomplete": skipped > 0,
                "scope": "OS-visible processes; no complete-host guarantee",
            },
        }

    def _top_processes(self) -> tuple[list[dict[str, Any]], int]:
        rows: list[dict[str, Any]] = []
        skipped = 0
        # No elevated privileges. A process may exit between these calls.
        for process in psutil.process_iter():
            try:
                rss = process.memory_info().rss
                name = process.name()
                rows.append({"pid": process.pid, "name": name,
                             "rss_bytes": rss,
                             "rss_mib": round(rss / 1024**2, 2)})
            except (psutil.NoSuchProcess, psutil.AccessDenied,
                    psutil.ZombieProcess) as exc:
                skipped += 1
                logger.warning("skip pid=%s; reason=%s",
                               process.pid, type(exc).__name__)
        rows.sort(key=lambda row: row["rss_bytes"], reverse=True)
        return rows[:self.top], skipped
