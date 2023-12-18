# Pandas Day 16
# Problem description:
# https://leetcode.com/problems/count-salary-categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    def classify( salary: int) -> str:
        if salary < 20000:
            return "Low Salary"
        elif salary <= 50000:
            return "Average Salary"
        else:
            return "High Salary"

    
    accounts['category'] = accounts.income.map(classify)

    grp_df = accounts.groupby(by="category", as_index=False).size()

    grp_df.rename(columns={"size" : "accounts_count"}, inplace=True)

    left_df = pd.DataFrame({"category" : ["Low Salary", "Average Salary", "High Salary"]})

    result_df = left_df.merge(grp_df, how="left", left_on="category", right_on="category")

    result_df.fillna(0, inplace=True)

    #result_df

    return result_df
