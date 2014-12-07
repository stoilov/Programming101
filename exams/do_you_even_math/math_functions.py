from sqlalchemy import create_engine, update, and_, desc
from models import Score
from sqlalchemy.orm import Session
from connect import Base
from random import randint


class Math:
    PLUS = "+"
    MINUS = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"
    POWER = "^"

    def __init__(self, session, player):
        engine = create_engine("sqlite:///scores.db")
        Base.metadata.create_all(engine)
        session = Session(bind=engine)

        self.session = session
        self.operations = [Math.PLUS, Math.MINUS, Math.MULTIPLICATION, Math.DIVISION, Math.POWER]
        self.score = 0
        self.player = player
        self.operation = {}

    def get_random_number(self):
        return randint(1, 10)

    def get_random_operation(self):
        index = randint(0, 4)
        return self.operations[index]

    def is_divisible(self, furst_number, second_number, operation):
        if furst_number % second_number == 0 and operation == Math.DIVISION:
            return True
        if operation != Math.DIVISION:
            return True
        return False

    def result(self, first_number, second_number, operation):
        if operation == Math.POWER:
            result = first_number ** second_number
        else:
            result = int(eval("{} {} {}".format(first_number, operation, second_number)))

        return str(result)

    def make_random_expression(self):
        while True:
            first_number = self.get_random_number()
            second_number = self.get_random_number()
            operation = self.get_random_operation()
            if self.is_divisible(first_number, second_number, operation):
                break

        output_string = "What is the answer to {} {} {}?"
        expression = output_string.format(first_number, operation, second_number)
        result = self.result(first_number, second_number, operation)
        self.operation = {"expression": expression, "result": result}

    def get_score(self):
        player_score = self.session.query(Score).filter(and_(
            Score.player == self.player, Score.score >= self.score
            )).all()
        if len(player_score) > 0:
            return {"has_played": True, "player_score": player_score[0].score}
        else:
            return {"has_played": False, "player_score": 0}

    def save_score(self, score):
        score_info = self.get_score()
        if score_info["has_played"] is True and score_info["player_score"] < score:
            self.session.query(Score).filter(Score.player == self.player).update({"score": score})
            self.session.commit()
        if score_info["has_played"] is False:
            score_object = Score(player=self.player, score=score)
            self.session.add(score_object)
            self.session.commit()

    def get_highscores(self):
        highscores = self.session.query(Score).order_by(desc(Score.score)).limit(10)
        return highscores
