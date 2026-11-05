import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__}: {elapsed:.6f}s")
    return wrapper

@timed
def sum_values(limit):
    return sum(range(limit))

print(sum_values(1000))     # 499500，另有一行实际耗时
