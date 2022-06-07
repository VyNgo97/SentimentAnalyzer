from sqlalchemy import Column, Integer, String, Float, DateTime

from .database import Base

# you can identify relationships between tables as well with sqlalchemy.org.relationship

class Movie(Base):
    __tablename__ == "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    sentiment = Column(Float, unique=False, index=True)
    date = Column(DateTime, unique=False, index=False)

class Game(Base):
    __tablename__ == "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    sentiment = Column(Float, unique=False, index=True)
    date = Column(DateTime, unique=False, index=False)
