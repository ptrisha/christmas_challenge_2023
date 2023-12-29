# Pandas problem Day 27
# Problem description:
# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    grouped_employees = employee.groupby("managerId", as_index=False).size()
    #grouped_employees - has columns: managerId, size

    # filter grouped_employees for those with size >= 5
    manager = grouped_employees[ grouped_employees["size"] >= 5]

    # merge manager with employee to get managers' names
    ans_df = manager.merge(employee, how="inner", left_on="managerId", right_on="id")

    ans_df = ans_df[['name']]

    return ans_df
