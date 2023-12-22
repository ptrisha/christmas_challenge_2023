# Pandas problem Day 20
# Problem description:
# https://leetcode.com/problems/classes-more-than-5-students

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classes = courses.groupby("class", as_index=False)["student"].count()
    classes
    classes = classes[ classes['student'] >= 5 ]

    classes.drop(["student"], axis=1, inplace=True)

    return classes

