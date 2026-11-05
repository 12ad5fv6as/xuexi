def high_values(values, threshold=80):
    for value in values:
        if value >= threshold:
            yield value

result = high_values([20, 80, 95])
print(next(result))        # 80
print(list(result))        # [95]
print(list(result))        # []

print(list(high_values([60, 80, 95])))
