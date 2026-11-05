def high_values(values,threshold=80):
	for value in values:
		if value >= threshold:
			yield value
result = high_values([20,80,95])
print(next(result))
print(list(result))
print(list(result))
