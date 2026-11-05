samples = [10.0, 20.0]
alias = samples
alias.append(30.0)
print("原列表:", samples)
print("别名:", alias)
print("是否同一对象:", alias is samples)
copied = samples.copy()
copied.append(40.0)
print("复制后原列表:", samples)
print("复制列表:", copied)
print("是否同一对象:", copied is samples)
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(5)
print("浅拷贝后原嵌套列表:", nested)
