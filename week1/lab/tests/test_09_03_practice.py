from monitor.rules import classify_usage

def test_boundary_is_high():
	result = classify_usage(80.0,threshold=80.0)
	assert result == "high"

