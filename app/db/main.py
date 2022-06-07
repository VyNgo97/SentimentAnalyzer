from sqlalchemy.orm import Session

import models
from ..schemas import movie, game

def get_movie(db: Session, movie_name: str):
    return db.query(models.Movie).filter(models.Movie.name == movie_name).first()

def get_game(db: Session, game_name: str):
    return db.query(models.Movie).filter(models.Movie.name == game_name).first()

def create_movie(db: Session, movie: movie.MovieCreate):
    db_movie = models.Movie(name=movie.name, sentiment=movie.sentiment, time=movie.time)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def create_movie(db: Session, game: game.GameCreate):
    db_game = models.Movie(name=game.name, sentiment=game.sentiment, time=game.time)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game