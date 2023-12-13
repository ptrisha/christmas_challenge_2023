# Pandas problem Day 11
# Problem description:
# https://leetcode.com/problems/second-highest-salary

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    salary_unique = set(employee['salary'])
    salary_unique_list = list(salary_unique)

    if len(salary_unique_list) < 2:
        ans = None
    else:
        sorted_sal = sorted(salary_unique_list, reverse=True)
        ans = sorted_sal[1]

    ans_df = pd.DataFrame({"SecondHighestSalary" : [ans]})

    return ans_df
