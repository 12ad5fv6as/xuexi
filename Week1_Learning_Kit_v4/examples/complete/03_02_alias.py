samples = [10.0, 20.0]
alias = samples
alias.append(30.0)
print("samples after alias.append:", samples)  # [10.0, 20.0, 30.0]
print("alias is samples:", alias is samples)   # True

copy = samples.copy()
copy.append(40.0)
print("samples after copy.append:", samples)  # [10.0, 20.0, 30.0]
print("copy:", copy)                          # [10.0, 20.0, 30.0, 40.0]
print("copy is samples:", copy is samples)    # False
print("len(samples):", len(samples))          # 3

# Shallow copy: a nested list is still shared.
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(5)
print("nested after shallow change:", nested)  # [[1, 2, 5], [3, 4]]
