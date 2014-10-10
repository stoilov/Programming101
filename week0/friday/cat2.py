# cat2.py
import sys

def main():
    for filename in sys.argv:
    	if filename != "cat2.py":
    		file = open(filename, 'r')
    		content = file.read()
    		print(content)

    file.close()

if __name__ == '__main__':
    main()

