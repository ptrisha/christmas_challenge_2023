# Pandas problem Day 23
# Problem description:
# https://leetcode.com/problems/daily-leads-and-partners

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    daily_sales.drop_duplicates(inplace=True)
    grouped =daily_sales.groupby(["date_id", "make_name"], as_index=False)[["lead_id", "partner_id"]].nunique()
    grouped.rename(columns={"lead_id": "unique_leads", "partner_id": "unique_partners"}, inplace=True)

    return grouped
