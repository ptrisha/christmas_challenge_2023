# Pandas Day 09
# Problem description:
# https://leetcode.com/problems/patients-with-a-condition/submissions

import pandas as pd

def check_diab(conditions: str) -> bool:
    split_parts = conditions.split(" ")
    return any([ cond.startswith("DIAB1") for cond in split_parts] )

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    patients['diab1'] = patients['conditions'].apply(check_diab)
    diab1_df = patients[ patients['diab1']==True ]
    diab1_df.drop('diab1', axis=1, inplace=True)
   
    return diab1_df
