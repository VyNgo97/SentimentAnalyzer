from pydantic import BaseModel
from datetime import date

class GameBase(BaseModel):
    '''Class representation of a game'''
    name: str
    sentiment: float
    time: date

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name: str) -> None:
    #     self._name = name

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int

    class Config:
        orm_mode = True