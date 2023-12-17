# Pandas problem Day 14
# Problem description:
# https://leetcode.com/problems/delete-duplicate-emails

# I feel that groupby should be used, but I could not get it to work.

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
     person.sort_values(by=["email", "id"], inplace=True)
     person.drop_duplicates(subset="email", keep="first", inplace=True)

