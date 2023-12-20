# Pandas problem Day 18
# Problem description:
# https://leetcode.com/problems/game-play-analysis-i

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    ans_df = activity.groupby('player_id', as_index=False).event_date.min()

    ans_df.rename(columns={'event_date': 'first_login'}, inplace=True)

    return ans_df

