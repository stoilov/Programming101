# pizza.py
import sys
from time import time
from datetime import datetime

persons = []
prices = []
time_stamps = []
saved_files = []
list_used = False

def take(name, price):
	msg = "Taking order from {} for {}".format(name, price)
	if name in persons:
		prices[persons.index(name)] += price

	else:
		persons.append(name)
		prices.append(price)

	print(msg)
	main()

def status():
	for i, k in enumerate(persons):
		msg = "{} - {}".format(persons[i], prices[i])
		print(msg)
		
	main()

def save():
	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
	stamp = "orders_" + stamp
	save_data = []
	for i, k in enumerate(persons):
		save_data.append("{} - {}".format(persons[i], prices[i]))

	file = open(stamp, "w")
	file.write("\n".join(save_data))
	file.close()
	saved_files.append(stamp)
	del persons[:]
	del prices[:]

	print("Saved the current order to {}".format(stamp))
	main()

def list_files():
	list_used = True
	for number, filename in enumerate(saved_files):
		msg = "[{}] - {}".format(number + 1, filename)
		print(msg)

	main()

def load(order_number):
	#not fully functional
	order_number -= 1
	if len(persons) == 0:
		file = open(saved_files[order_number], "r")
		for line in file:
			order_load = line.split(" - ")
			persons.append(order_load[0])
			prices.append(order_load[1])

		file.close()
	else:
		print("You have not saved the current order.\nIf you wish to discard it, type load <number> again.")
		main()

	if not list_used:
		print("Use list command before loading")
		main()



def finish():
	#not fully functional
	if len(persons) > 0:
		print("You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save")


def main():
	command = input("Enter command>")
	command = command.split(" ")

	if command[0] == "take":
		command[2] = float(command[2])
		command[2] = round(command[2], 2)
		take(command[1], command[2])

	elif command[0] == "status":
		status()

	elif command[0] == "save":
		save()

	elif command[0] == "list":
		list_files()

	elif command[0] == "load":
		if len(command) > 1:
			command[1] = int(command[1])
			permission_to_load = True
			load(command[1])

		else:
			main()

	elif command[0] == "finish":
		finish()

	else:
		print("Unknown command!\nTry one of the following:\ntake <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish")
		main()


if __name__ == "__main__":
	main()