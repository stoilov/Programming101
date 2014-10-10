def simply_fraction(fraction):
	nominator = fraction[0]
	denominator = fraction[1]

	for i in range(1, nominator + 1):
		if nominator % i == 0 and denominator % i == 0:
			nominator //= i
			denominator //= i

	return (nominator, denominator)

print(simply_fraction((63, 462)))