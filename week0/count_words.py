def count_words(arr):
	a = {}
	words_set = set(arr)
	for word in words_set:
		word_count = 0
		for i in arr:
			if word == i:
				word_count += 1
				a[word] = word_count

	return a