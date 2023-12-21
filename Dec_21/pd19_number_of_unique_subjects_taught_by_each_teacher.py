# Pandas problem Day 19
# Problem description:
# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    
    unique_count = teacher.groupby("teacher_id", as_index=False).nunique("subject_id")

    unique_count.drop("dept_id", axis=1, inplace=True)

    unique_count.rename(columns={"subject_id": "cnt"}, inplace=True )

    return unique_count

