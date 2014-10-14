def contains_digit(number, digit):
    if str(digit) in str(number):
        return True
    else:
        return False

print(contains_digit(1000, 0))
