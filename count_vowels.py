def count_vowels(str):
    vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
    result = 0
    for letter in str:
        if letter in vowels:
            result += 1

    return result
