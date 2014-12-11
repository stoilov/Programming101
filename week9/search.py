from sqlalchemy import create_engine
from models import Website, Pages
from sqlalchemy.orm import Session
from connect import Base


def main():
    engine = create_engine("sqlite:///search.db")

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    search = Search(session)


if __name__ == "__main__":
    main()
