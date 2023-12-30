# Pandas problem Day 28
# This is the last of the Pandas problems.
# Problem description:
# https://leetcode.com/problems/sales-person/

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # merge company and orders to get company name for each order
    merged = orders.merge(company, how="left", on="com_id")

    # keep only necessary columns
    company_orders = merged[["com_id", "order_id", "sales_id"] ]
    company_orders['com_name'] = merged["name"]

    # merge company_orders with salesperson
    salesperson_company = sales_person.merge(company_orders, how="left", on="sales_id")
    salesperson_company = salesperson_company[ ["sales_id", "name", "com_name"]]

    # group by sales person - and list the companies for each person
    grp = salesperson_company.groupby(["sales_id", "name"], as_index=False)["com_name"].unique()

    grp["red"] = grp["com_name"].apply(lambda x: "RED" in list(x))
    grp = grp[ grp["red"]==False ]

    grp_ans = pd.DataFrame({"name": grp["name"].unique()})

    return grp_ans
