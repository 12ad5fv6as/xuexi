samples = [10.0, 20.0]
alias = samples
alias.append(30.0)
print(samples)             # [10.0, 20.0, 30.0]

copy = samples.copy()
copy.append(40.0)
print(len(samples))       # 3
