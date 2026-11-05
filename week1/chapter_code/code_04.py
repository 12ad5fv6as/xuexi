def utilization(used: float,total: float) -> float:
    if total <= 0:
        raise ValueError("total must be positive")
    if used < 0 or used > total:
        raise ValueError("used must be between 0 and total")
    return round(used / total * 100, 2)

result = utilization(3,8)
print(result)
