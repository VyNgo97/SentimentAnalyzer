from locale import format_string
from fastapi import APIRouter
# import utils.reddit_api
import utils.sentiment_model
from datetime import date, datetime
import time
from schemas.movie import Movie
router = APIRouter()

# TODO: this is meant to first query the db for avengers and if no response then run analyze
# TODO: add back , response_model=Movie
@router.get('/movies/{movie}', status_code=200)
async def read_movies(movie: str):
    # return [{'name': 'The Avengers', 'sentiment': 2.3, 'time': datetime.now().strftime('%d/%m/%y')}]
    return utils.sentiment_model.analyze('movies', movie)