# Pandas problem Day 22
# Problem description:
# https://leetcode.com/problems/group-sold-products-by-the-date/

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    
    activities.drop_duplicates(inplace=True)
    grouped = activities.groupby(["sell_date"], as_index=False)["product"].unique()
    grouped["product"] = grouped["product"].apply(lambda x: sorted(x))
    grouped["num_sold"] = grouped["product"].apply(lambda x: len(x))
    grouped["product"] = grouped["product"].apply(lambda x: ",".join(x))
    
    grouped = grouped[ ["sell_date", "num_sold", "product"]]
    grouped.rename(columns={"product": "products"}, inplace=True)
     
    return grouped
