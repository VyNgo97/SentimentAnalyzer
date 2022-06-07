import requests
import typing
import logging

# Store these values in secret manager
SECRET: str = "CTtAV5nuayVKgwGlp7kNcmXalSYELQ"
ID: str = "VOijjXVJZWjtmR4hZ3S_lA"
USERNAME: str = "vyngotl"
PASSWORD: str = "todjux-bapnok-cubtU8"
BASE_URI: str = "https://oauth.reddit.com/r/"
TOP: str = "/top"

headers_default = {"User-Agent": "DataGrabber/0.0.1"}

# TODO: Check if token is expired


def get_auth_token(headers: typing.Dict[str, str]):
    auth = requests.auth.HTTPBasicAuth(ID, SECRET)
    data = {"grant_type": "password", "username": USERNAME, "password": PASSWORD}
    res = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data=data,
        headers=headers
    )
    token = res.json()["access_token"]
    return token


def get_reddit_data(subreddit: str, movie: str):
    # params = {"count": 1, "limit": 1}
    TOKEN = get_auth_token(headers_default)
    headers = {**headers_default, **{"Authorization": f"bearer {TOKEN}"}}
    params = {"limit": 50, **{"q": movie}}
    logging.info(f"Requesting data from the {subreddit} subreddit now...")
    data = requests.get("".join([BASE_URI, subreddit, '/search']), headers=headers, params=params)
    return data.json()
