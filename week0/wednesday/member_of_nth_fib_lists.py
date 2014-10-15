# I didn't get the task, so this does not work.

from nth_fib_lists import nth_fib_lists
from list_to_number import list_to_number

def member_of_nth_fib_lists(listA, listB, needle):
	fib_list = nth_fib_lists(listA, listB, 5)
	fib_list = list_to_number(fib_list)
	fib_list = str(fib_list)
	
	needle = list_to_number(needle)
	needle = str(needle)

	if needle in fib_list:
		return True

	return False