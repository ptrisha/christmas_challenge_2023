# Day 05 of 30 days of Panda
# Problem description:
# https://leetcode.com/problems/invalid-tweets

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    invalid_df = tweets[ tweets["content"].str.len() > 15]
    invalid_df.drop(['content'], axis=1, inplace=True)

    return invalid_df

