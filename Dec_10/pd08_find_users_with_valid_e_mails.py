# Pandas Day 08
# Problem description:
# https://leetcode.com/problems/find-users-with-valid-e-mails/

import pandas as pd

def check_email(email: str) -> bool:
    split_parts = email.rsplit('@', 1)
    if len(split_parts) != 2:
        return False
    prefix = split_parts[0].lower()
    domain = split_parts[1]
    if domain != "leetcode.com":
        return False
    if not prefix[0].isalpha():
        return False
    for c in prefix:
        if c.isalnum() or c in ['_', '.', '-']:
            pass
        else:
            return False
    return True


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    users['valid'] = users['mail'].apply(check_email)
    valid_df = users[ users['valid']==True ]
    valid_df.drop(["valid"], axis=1, inplace=True)

    return valid_df

