from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from connect import Base


class Score(Base):
    __tablename__ = "score_board"
    id = Column(Integer, primary_key=True)
    player = Column(String)
    score = Column(Float)

    def __str__(self):
        return "{} - {}".format(self.player, self.score)


def main():
    engine = create_engine("sqlite:///scores.db")

    Base.metadata.create_all(engine)
