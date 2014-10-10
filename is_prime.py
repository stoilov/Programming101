def is_prime(n):
    if n == 1 or n <= 0:
        return False

    br = 0
    for i in range(1, n):
        if n % i == 0:
            br += 1

    if br > 1:
        return False
    else:
        return True


