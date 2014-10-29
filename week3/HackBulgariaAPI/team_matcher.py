import requests
import random


class MatchCourse:

    def __init__(self):
        self.url = "https://hackbulgaria.com/api/students/"
        self.records = []
        self.courses = None

    def get_info(self):
        self.records = requests.get(self.url, verify=False)
        if self.records.status_code != 200:
            return False

        self.records = self.records.json()
        return self.records

    def print_messages(self):
        print("\nHello, you can use one the following commands")
        print("list_courses - this lists all the courses that are available now.")
        print("match_teams <course_id>, <team_size>, <group_time>\n\n")

    def list_courses(self):
        if self.records is False:
            return False

        self.courses = set()
        for record in self.records:
            for course in record["courses"]:
                self.courses.add(course["name"])

        self.courses = list(self.courses)
        for key, course in enumerate(self.courses):
            print("[{}] {}".format(key + 1, course))

    def match_teams(self, course_id, team_size, group_time):
        people_in_teams = []
        for record in self.records:
            for course in record["courses"]:
                course_group = course["group"] == group_time
                course_name = course["name"] == self.courses[course_id - 1]
                available = record["available"] is True
                if course_name and course_group and available:
                    people_in_teams.append(record["name"])

        random.shuffle(people_in_teams)
        for key, student in enumerate(people_in_teams):
            print(student)
            if (key + 1) % team_size == 0:
                print("==========")

    def get_input(self):
        command = input("Enter command> ")
        command = command.split(" ")
        return command

    def interface(self):
        command = self.get_input()
        while command[0] != "exit":
            if command[0] == "list_courses":
                self.list_courses()
                command = self.get_input()
            elif command[0] == "match_teams":
                command[1] = int(command[1])
                command[2] = int(command[2])
                command[3] = int(command[3])
                self.match_teams(command[1], command[2], command[3])
                command = self.get_input()
            else:
                print("Bad input!")
                command = self.get_input()
        else:
            print("Goodbye!")


def main():
    hackbulgaria = MatchCourse()
    hackbulgaria.get_info()
    hackbulgaria.print_messages()
    hackbulgaria.interface()


if __name__ == "__main__":
    main()
