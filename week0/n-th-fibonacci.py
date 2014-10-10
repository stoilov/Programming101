def nth_fibonacci(n):
    first = 1
    second = 1
    current = 0
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(2, n):
            current = first + second
            first = second
            second = current

    return current

def main():
    print(nth_fibonacci(10))

if __name__ == "__main__":
    main()
