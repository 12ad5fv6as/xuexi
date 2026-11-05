"""Run with Python; predict the output before execution."""
samples = [10.0, 20.0]
alias = samples
alias.append(30.0)
print(samples)
for percent in [35.0, 80.0, 92.5]:
    print(percent, "high" if percent >= 80 else "normal")
