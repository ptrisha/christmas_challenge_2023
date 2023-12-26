# Pandas problem Day 24
# Problem description:
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

# The Leetcode problems challenge ended on Dec 25.  I'm continuing with the Pandas
# problems till Dec 30.

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    grouped = actor_director.groupby(["actor_id", "director_id"], as_index=False)["timestamp"].count()
    #grouped

    ans_df = grouped[ grouped["timestamp"] >= 3 ]
    ans_df.drop(["timestamp"], axis=1, inplace=True)

    return ans_df
