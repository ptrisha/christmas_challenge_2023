# Pandas problem Day 17 (Dec 19)
# Problem description:
# https://leetcode.com/problems/find-total-time-spent-by-each-employee/

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    # compute a column of the time difference (in min)
    employees['total_time'] = employees['out_time'] - employees['in_time']

    # group by emp_id and event_day and sum time_span for each group
    employees = employees.groupby(['emp_id','event_day'], as_index=False)['total_time'].sum()

    #employees.drop(['in_time', 'out_time'], axis=1, inplace=True)

    employees.rename(columns={"event_day": "day"}, inplace=True)

    return employees

