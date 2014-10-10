# generate_numbers.py
import sys
from random import randint


def main():
    file = open(sys.argv[1], 'w')
    n = int(sys.argv[2])
    numbers = []
    for i in range(n):
    	numbers.append(str(randint(1, 1000)))

    file.write(" ".join(numbers))
    file.close()

if __name__ == '__main__':
    main()
