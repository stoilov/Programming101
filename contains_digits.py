def contains_digits(number, digits):
    return_value = True
    for i in digits:
        if str(i) not in str(number):
            return_value = False

    return return_value

print(contains_digits(456, []))
