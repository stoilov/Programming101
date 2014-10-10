def prepare_meal(number):
	result = ''

	if number % 5 == 0:
		result += "and eggs"
	
	while number % 3 == 0:
		result = "spam " + result
		number //= 3

	return result