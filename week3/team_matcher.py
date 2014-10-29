import requests
from students import Student


class MatchCourse:

    def __init__(self):
        self.url = "https://hackbulgaria.com/api/students/"
        self.students = []

    def get_info(self, url):
        records = requests.get(url, verify=False)
        if records.status_code != 200:
            return False

        records = records.json()

        for record in records:
            student_name = record["name"]
            student_available = record["available"]
            student_courses = record["courses"]
            student = Student(student_name, student_available, student_courses)
            self.students.append(student)

        return records

    def list_courses(self):
        records = self.get_info(self.url)
        if records is False:
            return False

        courses = set()
        for course in self.students:
            for name, course_name in course.courses:
                if name == "name":
                    print(course_name)



        courses = list(courses)
        return courses


def main():
    hackbulgaria = MatchCourse()
    print(hackbulgaria.list_courses())

if __name__ == "__main__":
    main()
