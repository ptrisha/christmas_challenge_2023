# Pandas problem Day 12
# Problem description:
# https://leetcode.com/problems/department-highest-salary/

# This version needs optimization.

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    idx = employee.groupby('departmentId')['salary'].idxmax()
    max_salaries_unique = employee.loc[idx][ ['departmentId', 'salary']]
    max_salaries = employee.merge( max_salaries_unique, how="inner", on=['departmentId', 'salary'] )

    #print(max_salaries)

    merged_df = max_salaries.merge( department, how="left", left_on="departmentId", right_on="id")
    merged_df.drop(['id_x', 'departmentId', 'id_y'], axis=1, inplace=True)
    merged_df.rename(columns={"salary": "Salary", "name_y": "Department", "name_x": "Employee"}, inplace=True)

    return merged_df

