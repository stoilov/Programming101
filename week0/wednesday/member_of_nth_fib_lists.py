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

<<<<<<< HEAD:week0/wednesday/member_of_nth_fib_lists.py
	return False
=======
	return False

print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
>>>>>>> fd992b8fd2a6f2779759369d25c31dff4ce87951:week0/member_of_nth_fib_lists.py
