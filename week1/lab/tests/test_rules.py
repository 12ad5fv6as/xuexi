import pytest
from monitor.rules import classify_usage


@pytest.mark.parametrize("value, threshold, expected", [
    (0, 80, "normal"), (79.9, 80, "normal"), (80, 80, "high"),
    (100, 80, "high"), (0, 0, "high"), (99.9, 100, "normal"),
    (100, 100, "high"),
])
def test_usage(value, threshold, expected):
    assert classify_usage(value, threshold) == expected


@pytest.mark.parametrize("value", [-1, 101, float("nan"),
                                  float("inf"), "80", True, None])
def test_invalid_percentage(value):
    with pytest.raises(ValueError):
        classify_usage(value)


@pytest.mark.parametrize("threshold", [-1, 101, float("nan")])
def test_invalid_threshold(threshold):
    with pytest.raises(ValueError):
        classify_usage(50, threshold)
