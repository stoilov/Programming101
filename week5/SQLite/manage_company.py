import sqlite3


def list_employees(cursor, db):
    employee_represent = ""
    employees = cursor.execute('''SELECT id, name, position FROM company''')
    for row in employees:
        employee_represent += "{id} - {name} - {position}\n".format(**row)

    return employee_represent


def monthly_spending(cursor, db):
    get_sum = cursor.execute('''SELECT SUM(monthly_salary) AS total_sum FROM company''')
    for row in get_sum:
        total_sum = row["total_sum"]

    return total_sum


def yearly_spending(cursor, db):
    MONTHS = 12
    bonus_sum = cursor.execute('''SELECT SUM(monthly_salary) AS total_sum FROM company''')
    for row in bonus_sum:
        yearly_bonuses = row["total_sum"]

    salaries = monthly_spending(cursor, db) * MONTHS
    return salaries + yearly_bonuses


def add_employee(cursor, db, name, salary, bonus, position):
    cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
             VALUES(?, ?, ?, ?)''', (name, salary, bonus, position))
    db.commit()


def delete_employee(cursor, db, employee_id):
    cursor.execute('''DELETE FROM company WHERE id=(?)''', (employee_id,))
    db.commit()


def update_employee(cursor, db ,employee_id, name, salary, bonus, position):
    cursor.execute('''UPDATE company
             SET name=?, monthly_salary=?, yearly_bonus=?, position=? 
             WHERE id=?''', (name, salary, bonus, position, employee_id))
    db.commit()


def get_input():
    command = input("Enter command> ")
    command = command.split(" ")
    return command


def interface(cursor, db):
    command = get_input()
    while command[0] != "exit":
        if command[0] == "list_employees":
            print(list_employees(cursor, db))
            command = get_input()
        elif command[0] == "monthly_spending":
            monthly_total = monthly_spending(cursor, db)
            print("The company is spending ${} every month!".format(monthly_total))
            command = get_input()
        elif command[0] == "yearly_spending":
            yearly_total = yearly_spending(cursor, db)
            print("The company is spending ${} every year!".format(yearly_total))
            command = get_input()
        elif command[0] == "add_employee":
            name = input("name> ")
            monthly_salary = int(input("monthly_salary> "))
            yearly_bonus = int(input("yearly_bonus> "))
            position = input("position> ")
            add_employee(cursor, db, name, monthly_salary, yearly_bonus, position)
            command = get_input()
        elif command[0] == "delete_employee":
            employee_id = int(command[1])
            delete_employee(cursor, db, employee_id)
            command = get_input()
        elif command[0] == "update_employee":
            employee_id = int(command[1])
            name = input("name> ")
            monthly_salary = int(input("monthly_salary> "))
            yearly_bonus = int(input("yearly_bonus> "))
            position = input("position> ")
            update_employee(cursor, db, employee_id, name, monthly_salary, yearly_bonus, position)
            command = get_input()
        else:
            print("Bad input!")
            command = get_input()
    else:
        print("Goodbye!")


def main():
    db = sqlite3.connect('company.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    interface(cursor, db)
    company.interface()
    db.close()

if __name__ == '__main__':
    main()
