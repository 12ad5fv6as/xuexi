"""Three mechanisms, with no network or privileged operations."""
import time
from functools import wraps
from contextlib import contextmanager

def high_values(values, threshold=80):
    for value in values:
        if value >= threshold:
            yield value

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__}: {time.perf_counter()-start:.6f}s")
    return wrapper

@contextmanager
def experiment(name):
    print("begin:", name)
    try:
        yield
    finally:
        print("end:", name)

@timed
def answer():
    return 42

if __name__ == "__main__":
    values = high_values([20, 80, 95])
    print(next(values), list(values), list(values))
    with experiment("mechanisms"):
        assert answer() == 42
