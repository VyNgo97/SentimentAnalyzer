from pydantic import BaseModel
from datetime import date

class MovieBase(BaseModel):
    '''Class representation of a movie'''
    name: str
    sentiment: float
    time: date

# this is the model used to create the user
class MovieCreate(MovieBase):
    pass

# this is the model used when pulling the data from the db- notice how we now know the ID since it is in the db after creation
class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True