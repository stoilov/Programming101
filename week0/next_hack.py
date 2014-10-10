from is_int_palindrome import is_int_palindrome
from count_substrings import count_substring

def next_hack(n):
    next_found = False
    while not next_found:
        n += 1
        if is_int_palindrome(int(bin(n)[2:])) and count_substring(bin(n), "1") % 2 == 1:
             next_found = True

    return n
