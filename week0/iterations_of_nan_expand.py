def iterations_of_nan_expand(expanded):
	a = expanded.split(" ")
	last_word = a.pop()
	only_not = len(set(a[::2]))
	only_a = len(set(a[1::2]))
	if only_not == 1 and only_a == 1 and a[0] == "Not" and a[1] == "a" and last_word == "NaN":
		return len(a) // 2
	return False