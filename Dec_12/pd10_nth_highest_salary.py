# Pandas Day 10
# Problem description:
# https://leetcode.com/problems/nth-highest-salary/

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], inplace=True)
    if N > len(employee):
        ans = None
    else:
        sorted_sal = employee.sort_values(by='salary', ascending=False)
        ans = sorted_sal.iloc[N-1]['salary']
    
    col_name = "getNthHighestSalary("+str(N)+")"
    ans_df = pd.DataFrame({col_name: [ans]})

    return ans_df
  
