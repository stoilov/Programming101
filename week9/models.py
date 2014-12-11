from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from connect import Base


class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    pages = relationship("Pages")
    title = Column(String)
    domain = Column(String)
    pages_count = Column(Integer)


class Pages(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    website = Column(Integer, ForeignKey("website.id"))
    date = Column(DateTime)
    url = Column(String)
    title = Column(String)
    desc = Column(String)
    ads = Column(Integer)
    SSL = Column(Integer)


def main():
    engine = create_engine("sqlite:///search.db")

    Base.metadata.create_all(engine)

    Session(bind=engine)

if __name__ == "__main__":
    main()
