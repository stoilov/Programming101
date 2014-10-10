# cat.py
import sys

def main():
	to_read = sys.argv[1]
	file = open(to_read, 'r')
	content = file.read()

	print(content)

	file.close()


if __name__ == "__main__":
	main()