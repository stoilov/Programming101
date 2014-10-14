# pizza.py
import sys
from time import time
from datetime import datetime
import os.path

persons = []
prices = []
time_stamps = []
used_commands = []
files_to_save = []
if os.path.exists("saved_files"):
	file = open("saved_files", "r")
	files_to_save = file.read().split("\n")
	file.close()

def take(name, price):
	msg = "Taking order from {} for {}".format(name, price)
	if name in persons:
		prices[persons.index(name)] = float(prices[persons.index(name)])
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
	files_to_save.append(stamp)
	save_data = []
	for i, k in enumerate(persons):
		save_data.append("{} - {}".format(persons[i], prices[i]))

	file = open(stamp, "w")
	file.write("\n".join(save_data))
	file.close()
	file = open("saved_files", "w")
	file.write("\n".join(files_to_save))
	file.close()
	del persons[:]
	del prices[:]

	print("Saved the current order to {}".format(stamp))
	main()

def list_files():
	if os.path.exists("saved_files"):
		file = open("saved_files", "r")
		saved_files = file.read().split("\n")
		file.close()
	else:
		saved_files = []

	for i, saved in enumerate(saved_files):
		msg = "[{}] - {}".format(i + 1, saved)
		print(msg)

	main()

def load(order_number):
	file = open("saved_files", "r")
	saved_files = file.read().split("\n")
	file.close()
	order_number -= 1
	if "list" not in used_commands:
		print("Use list command before loading")
		main()

	if used_commands[len(used_commands) - 2] == "load":
		del persons[:]
		del prices[:]

	if len(persons) > 0:
		print("You have not saved the current order.\nIf you wish to discard it, type load <number> again.")
		main()
	
	else:
		file = open(saved_files[order_number], "r")
		load_order_from_file = file.read().split("\n")
		for line in load_order_from_file:
			order_load = line.split(" - ")
			persons.append(order_load[0])
			prices.append(order_load[1])

		file.close()
		main()



def finish():
	if used_commands[len(used_commands) - 2] == "finish":
		del persons[:]
		del prices[:]

	if len(persons) > 0:
		print("You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save")
		main()
	else:
		print("Finishing order. Goodbye!")


def main():
	command = input("Enter command>")
	command = command.split(" ")
	used_commands.append(command[0])

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