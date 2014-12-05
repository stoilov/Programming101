from math_functions import Math
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from connect import Base


class Interface:

    def __init__(self, math):
        self.math = math
        self.player = ""
        self.score = 0

    def start_game(self):
        print("Welcome to the \"Do you even math?\" game!")
        print("Here are your options:")
        print("- start\n- highscores")
        self.get_command()

    def get_command(self):
        while True:
            command = input("?>")
            if command == "start":
                self.ask_questions()
            elif command == "highscores":
                self.show_highscores()
            else:
                print("There is not such command.")
                self.get_command()

    def get_player_name(self):
        name = input("Choose your name: ")
        return name

    def answer_input(self):
        while True:
            try:
                user_answer = int(input("?>"))
                break
            except ValueError:
                print("Please enter an integer value.")

        return str(user_answer)

    def do_the_math(self, math):
        self.math.make_random_expression()
        print(self.math.operation["expression"])
        user_answer = self.answer_input()

        return user_answer == math.operation["result"]

    def ask_questions(self):
        self.math.player = self.get_player_name()

        while self.do_the_math(self.math):
            self.math.score += 1
            print("?>Correct!")
        else:
            score = self.math.score * self.math.score
            print("Incorrect! Ending game. You score is: {}".format(score))
            self.math.save_score(score)
            self.math.score = 0

    def show_highscores(self):
        print("Highscores: ")
        highscores = self.math.get_highscores()
        for highscore in highscores:
            print(highscore)


def main():
    engine = create_engine("sqlite:///scores.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    new_player = ""

    math = Math(session, new_player)

    interface = Interface(math)
    interface.start_game()

if __name__ == "__main__":
    main()
