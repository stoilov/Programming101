# concat_files.py
import sys

def main():
	content = []
	sys.argv.pop(0)
	for in_file in sys.argv:
		file = open(in_file, 'r')
		current_content = file.read()
		content.append(current_content)
		file.close()

	file = open('MEGATRON', 'w')
	file.write("\n".join(content))
	file.close()


if __name__ == "__main__":
	main()