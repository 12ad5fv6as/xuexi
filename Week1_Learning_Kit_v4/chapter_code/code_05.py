def is_high_usage(percent: float, threshold: float = 80.0) -> bool:
    return percent >= threshold

print(is_high_usage(85.0))
print(is_high_usage(85.0, threshold=90.0))
