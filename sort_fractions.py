def sort_fractions(fractions):
	result = []
	calculated = []
	for fraction in fractions:
		value = fraction[0] / fraction[1]
		calculated.append([value, fraction])

	calculated.sort()

	for fraction in calculated:
		result.append(fraction[1])

	return result

print(sort_fractions([(2, 3), (1, 2), (1, 3)]))