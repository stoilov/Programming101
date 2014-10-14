from is_prime import is_prime

def prime_factorisation(n):
    if n == 1:
         return 1
   
    primes = []
    result = []
    
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    for p in primes:
        counter = 0
        if p * p > n:
             break

        while n % p == 0:
            counter += 1
            prime_factor = (p, counter)
            n //= p

        result.append(prime_factor)

    if n > 1:
        result.append(n)
 
    return result

print(prime_factorisation(1000))
