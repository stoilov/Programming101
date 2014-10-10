def count_consonants(str):
    consonants = list("bcdfghjklmnpqrstvwxz" + "bcdfghjklmnpqrstvwxz".upper())
    result = 0
    for letter in str:
        if letter in consonants:
            result += 1

    return result
