import pandas as pd
import utils.reddit_api
import logging
import json
import typing

def parse_data_to_df(subreddit: str, movie: str):
    data = utils.reddit_api.get_reddit_data(subreddit, movie)
    # write_data_to_file(data)
    df = pd.json_normalize(data['data']['children'])
    col = ['data.id', 'data.title', 'data.selftext']
    return df.loc[:, col]

def write_data_to_file(data: typing.Dict):
    json_string = json.dumps(data)
    file = open('app/data/test_data.json', 'w')
    file.write(json_string)
    file.close()

