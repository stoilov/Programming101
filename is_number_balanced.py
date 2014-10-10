from sum_of_digits import sum_of_digits
def is_number_balanced(n):
    right_side = n % (10 ** (len(str(n)) // 2))
    if len(str(n)) % 2 == 0:
        left_side = n // (10 ** (len(str(n)) // 2))
    else:
        left_side = n // (10 ** (len(str(n)) // 2 + 1))
       
    if sum_of_digits(left_side) == sum_of_digits(right_side):
         return True
    else:
         return False

print(is_number_balanced(156912))
