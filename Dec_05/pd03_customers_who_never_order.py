# This is day 3 of the Leetcode 30 Days of Panda.
# Link to problem description: 
# https://leetcode.com/problems/customers-who-never-order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # rename id column of customers df to "customerid"
    customers.rename(columns={"id": "customerId"}, inplace=True)

    # left merge on customerid columns
    result = pd.merge(customers, orders, how="left", on="customerId")
    no_order_customers = result[ result["id"].isnull() ]
    no_order_customer_names = pd.DataFrame({"Customers": no_order_customers.name})

    return no_order_customer_names
