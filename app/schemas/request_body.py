from pydantic import BaseModel, validator, ValidationError

subreddits = ['movies', 'games']

class RequestBody(BaseModel):
    subreddit: str
    name: str

    # cls is used in place of self for class methods (methods not specific to an object)
    @validator('subreddit')
    def subreddit_must_exist(cls, subreddit):
        # if we choose to use a drop down on the client side, this validator can go away
        if subreddit not in subreddits:
            raise ValueError('The subreddit entered does not exist')
        return subreddit

# try:
#     req = RequestBody(subreddit = 'movie', movie = 'Avengers')
#     print(req)
# except ValidationError as e:
#     print(e)