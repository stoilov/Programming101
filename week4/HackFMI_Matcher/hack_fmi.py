import csv
from datetime import datetime


class HackFMI:
    MENTOR_INDICATE = "### "
    CSV_DELIMITER = " | "
    MENTOR_INDEXES = range(1, 6)
    DATE_INDEX = 6
    MAXIMUM_TEAMS = 5
    MENTOR_NAME = 0
    MENTOR_TEAMS = 1

    def __init__(self):
        self.mentors = []
        self.teams = []

    def parse_mentors_from_markdown(self, filename):
        file = open(filename, "r")
        content = file.read().split("\n")
        file.close()
        for line in content:
            if HackFMI.MENTOR_INDICATE in line:
                mentor = []
                mentor.append(line.split(HackFMI.MENTOR_INDICATE)[1])
                mentor.append([])
                self.mentors.append(mentor)

    def make_datetime(self, datetime_str):
        date_time = datetime_str.split(" ")
        date = date_time[0].split(".")
        time = date_time[1].split(":")
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        hours = int(time[0])
        minutes = int(time[1])
        date_time = datetime(year, month, day, hours, minutes)
        return date_time

    def sort_teams_by_datetime(self):
        self.teams = sorted(self.teams, key=lambda k: k["date"])

    def load_teams_from_csv(self, filename):
        with open(filename, newline="") as csvfile:
            teams = csv.reader(csvfile)
            for row in teams:
                team_list = row[0].split(HackFMI.CSV_DELIMITER)
                team_dict = dict()
                team_dict["name"] = team_list[0]
                for mentor in HackFMI.MENTOR_INDEXES:
                    team_dict[mentor] = team_list[mentor]

                date = self.make_datetime(team_list[HackFMI.DATE_INDEX])
                team_dict["date"] = date
                self.teams.append(team_dict)

        self.sort_teams_by_datetime()

    def asign_teams(self):
        mentor_choice = 1
        team_index = 0
        while team_index < len(self.teams):
            team = self.teams[team_index]
            current_mentor = team[mentor_choice]
            current_mentor_list = [mentor[HackFMI.MENTOR_TEAMS] for mentor in self.mentors if mentor[HackFMI.MENTOR_NAME] == current_mentor]
            current_mentor_list = current_mentor_list[0]
            if len(current_mentor_list) < HackFMI.MAXIMUM_TEAMS:
                for mentor in self.mentors:
                    mentor_verified = mentor[HackFMI.MENTOR_NAME] == current_mentor
                    teams_verified = mentor[HackFMI.MENTOR_TEAMS] == current_mentor_list
                    if mentor_verified and teams_verified:
                        mentor[HackFMI.MENTOR_TEAMS].append(team["name"])
                        team_index += 1
                        mentor_choice = 1
            else:
                mentor_choice += 1

    def __str__(self):
        ouput = ""
        for mentor in self.mentors:
            if len(mentor[HackFMI.MENTOR_TEAMS]) > 0:
                ouput += mentor[HackFMI.MENTOR_NAME] + "\n-- "
                ouput += "\n-- ".join(mentor[HackFMI.MENTOR_TEAMS])
                ouput += "\n\n"

        return ouput


def main():
    hack_fmi = HackFMI()
    hack_fmi.parse_mentors_from_markdown("mentors.md")
    hack_fmi.load_teams_from_csv("teams.csv")
    hack_fmi.asign_teams()
    print(hack_fmi)

if __name__ == '__main__':
    main()
