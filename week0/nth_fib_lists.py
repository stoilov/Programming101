def nth_fib_lists(listA, listB, n):
	result = []
	if n == 1:
		return listA
	elif n == 2:
		return listB
	else:
		for i in range(3, n + 1):
			result = listA + listB
			listA = listB
			listB = result

	return result