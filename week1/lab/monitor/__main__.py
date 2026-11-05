"""Entry point: run from project root with python -m monitor."""
import argparse
import logging
import sys
from pathlib import Path

import psutil
from monitor.collector import SystemCollector
from monitor.storage import save_json

logger = logging.getLogger("monitor")


def close_logging() -> None:
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()


def configure_logging(path: Path) -> None:
    close_logging()
    path.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week 1 system snapshot")
    parser.add_argument("--output", type=Path,
                        default=Path("reports/system_report.json"))
    parser.add_argument("--log-file", type=Path,
                        default=Path("logs/monitor.log"))
    parser.add_argument("--disk-path", default="/")
    parser.add_argument("--interval", type=float, default=0.5)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--cpu-threshold", type=float, default=80.0)
    args = parser.parse_args(argv)
    try:
        if args.output.resolve() == args.log_file.resolve():
            raise ValueError("output and log-file must be different")
        # Logging setup can fail too; keep it inside this error boundary.
        configure_logging(args.log_file)
        collector = SystemCollector(args.disk_path, args.interval,
                                    args.top, args.cpu_threshold)
        logger.info("sampling started; interval=%s", args.interval)
        report = collector.collect()
        save_json(report, args.output)
        logger.info("report saved to %s", args.output)
        metrics = report["metrics"]
        print(f"Report: {args.output}")
        print(f"CPU: {metrics['cpu_percent']}% | "
              f"Memory: {metrics['memory_percent']}% | "
              f"Disk: {metrics['disk_percent']}%")
        print("Unreadable processes:",
              report["process_collection"]["skipped_count"])
        return 0
    except (OSError, ValueError, psutil.Error) as exc:
        if logger.handlers:
            logger.exception("sampling or persistence failed")
        print(f"Sampling failed: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 1
    finally:
        close_logging()


if __name__ == "__main__":
    raise SystemExit(main())
