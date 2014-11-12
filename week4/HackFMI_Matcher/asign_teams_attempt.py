def asign_teams(self):
    team_number = 0
    asigned_teams = []
    mentor_number = 1
    while len(asigned_teams) < len(self.teams):
        mentor = self.teams[team_number][mentor_number]
        mentor_list = [person["teams"] for person in self.mentors if person["name"] == mentor]
        if len(mentor_list) < HackFMI.MAXIMUM_TEAMS:
            self.mentors[mentor_number]["teams"].append(self.teams[team_number]["name"])
            asigned_teams.append(self.teams[team_number]["name"])
            team_number += 1
            mentor_number = 1
        else:
            mentor_number += 1