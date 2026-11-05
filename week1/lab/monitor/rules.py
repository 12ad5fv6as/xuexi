"""Small, deterministic business rules suitable for unit tests."""
import math


def validate_percentage(value: float, name: str = "percent") -> None:
    """Accept finite int/float percentages, rejecting bool and other types."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    if not math.isfinite(value) or not 0 <= value <= 100:
        raise ValueError(f"{name} must be finite and between 0 and 100")


def classify_usage(percent: float, threshold: float = 80.0) -> str:
    """Return a classroom rule label, NOT a diagnosis of hardware health."""
    validate_percentage(percent)
    validate_percentage(threshold, "threshold")
    return "high" if percent >= threshold else "normal"
