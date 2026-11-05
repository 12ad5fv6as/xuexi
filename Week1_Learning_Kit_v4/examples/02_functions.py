"""A minimal finite-number classroom example, not general input parsing."""
def utilization(used: float, total: float) -> float:
    if total <= 0:
        raise ValueError("total must be positive")
    if used < 0 or used > total:
        raise ValueError("used must be between zero and total")
    return round(used / total * 100, 2)

if __name__ == "__main__":
    assert utilization(3, 8) == 37.5
    print(utilization(3, 8))
