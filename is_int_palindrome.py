def is_int_palindrome(n):
    m = 0
    copy_n = n
    while copy_n > 0:
        m *= 10
        m += copy_n % 10
        copy_n //= 10
        
    if m == n:
        return True
    else:
        return False
