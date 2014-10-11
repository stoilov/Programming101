# wc.py
import sys

def main():
	file = open(sys.argv[2], "r")
	content = file.read()
	if sys.argv[1] == "chars":
		print(len(content))

	elif sys.argv[1] == "words":
		print(len(content.split(" ")))

	elif sys.argv[1] == "lines":
		lines = content.count("\n")

		print(lines)
		
	else:
		print("No such argument")

	file.close()


if __name__ == "__main__":
	main()