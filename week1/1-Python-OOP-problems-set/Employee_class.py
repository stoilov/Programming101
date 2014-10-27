class Employee:

    def __init_(self, name, salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def weeklyPay(self, hours):
        regular_pay = 40 * self.salary

        if hours > 40:
            return regular_pay + (hours - 40) * 1.5 * self.salary
        return regular_pay


class SalariedEmployee(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def weeklyPay(self, hours):
        return self.salary / 52


class Manager(Employee):

    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def weeklyPay(self, hours):
        return self.salary / 52 + self.bonus


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
