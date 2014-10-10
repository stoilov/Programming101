def groupby(func, seq):
	result = {}

	for item in seq:
		key = func(item)

		if key in result:
			result[key].append(item)
		else:
			result[key] = [item]

	return result

print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))