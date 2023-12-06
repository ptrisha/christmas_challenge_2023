# This is day 4 of the Leetcode 30 Days of Panda.
# Link to problem description: 
# https://leetcode.com/problems/article-views-i

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    author_viewers = views[ views.author_id==views.viewer_id ]

    author_viewers.drop(['article_id', 'viewer_id', 'view_date'], axis=1, inplace=True)

    author_viewers.drop_duplicates(inplace=True)

    author_viewers.rename(columns={"author_id": "id"}, inplace=True)


    return author_viewers.sort_values(by="id")
