# sum_numbers.py
import sys

def main():
	sum_integers = 0
	file = open(sys.argv[1], 'r')
	numbers = file.read()
	numbers = numbers.split(" ")
	
	for number in numbers:
		number = int(number)
		sum_integers += number

	file.close()
	print(sum_integers)


if __name__ == "__main__":
	main()