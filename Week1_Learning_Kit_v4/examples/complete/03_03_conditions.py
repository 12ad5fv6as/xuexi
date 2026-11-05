samples = [35.0, 80.0, 92.5]
for percent in samples:
    if percent >= 80.0:
        state = "high"
    else:
        state = "normal"
    print(percent, state)
