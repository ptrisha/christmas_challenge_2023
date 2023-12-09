# Pandas Day 06
# Problem description:
# https://leetcode.com/problems/calculate-special-bonus

import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    #np.where(condition, value_if_true, value_if_false)
 
    employees['bonus'] = np.where( (employees.employee_id%2==1) & (employees.name.str.startswith('M')==False), employees.salary, 0)
    employees.drop(['name', 'salary'], axis=1, inplace=True)
    employees.sort_values(by='employee_id', inplace=True)

    return employees
