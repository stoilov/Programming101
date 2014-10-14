def sum_of_digits(n):
    n = abs(n)
    result = 0
    while n > 0:
        a = n % 10
        result += a
        n = n // 10

    return result
