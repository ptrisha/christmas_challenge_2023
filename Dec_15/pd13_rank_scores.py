# Pandas problem Day 13
# Problem description:
# https://leetcode.com/problems/rank-scores

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    # create a dataframe with the scores in descending order and ranks
    scores_unique = list( scores['score'].unique())
    sorted_scores = sorted(scores_unique, reverse=True)
    
    rank = [ i+1 for i in range(len(sorted_scores))]

    rank_df = pd.DataFrame({"score" : sorted_scores, "rank" : rank })

    # sort the score df in descending order of score
    scores.sort_values(by="score", ascending=False, inplace=True)

    # merge the sorted scores df with the score_ranks df
    merged=scores.merge(rank_df, how="left", left_on="score", right_on="score")

    ans_df = merged[["score", "rank"]]

    return ans_df

