import pytest
from monitor.rules import classify_usage

@pytest.mark.parametrize("value, expected", [
    (79.9, "normal"),
    (80.0, "high"),
    (100.0, "high"),
])
def test_threshold_cases(value, expected):
    assert classify_usage(value) == expected

def test_invalid_percentage():
    with pytest.raises(ValueError):
        classify_usage(-1.0)
