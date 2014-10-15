def is_an_bn(word):
	half_len = len(word) // 2
	left_side = word[:half_len]
	right_side = word[half_len:]
	if left_side == "a" * half_len and right_side == "b" * half_len:
		return True
	
	return False

print(is_an_bn("aaabbb"))