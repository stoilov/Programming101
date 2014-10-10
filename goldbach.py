from is_prime import is_prime

def goldbach(n):
	if n <= 2:
		return False

	primes = []
	result = []

	for i in range(1, n):
		if is_prime(i):
			primes.append(i)

	for prime in primes:
		for another_prime in primes:
			if prime + another_prime == n and prime <= another_prime:
				result.append((prime, another_prime))

	return result