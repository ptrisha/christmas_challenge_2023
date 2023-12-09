# Day 07 of Pandas challenge
# Problem description:
# https://leetcode.com/problems/fix-names-in-a-table/

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.lower()
    users['name'] = users['name'].str.capitalize()
    users.sort_values(by='user_id', inplace=True)

    return users

