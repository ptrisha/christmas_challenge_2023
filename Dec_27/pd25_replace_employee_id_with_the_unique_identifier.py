# Pandas problem Day 25
# Problem description:
# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    employees_uniqueid = employees.merge(employee_uni, how="left", on="id")
    employees_uniqueid.drop("id", axis=1, inplace=True)

    return employees_uniqueid

