# Pandas problem Day 21
# Problem description:
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    orders_by_customer = orders.groupby("customer_number", as_index=False)["order_number"].count()
    orders_by_customer.sort_values(by="order_number", ascending=False, inplace=True)
    largest_customer = orders_by_customer.drop("order_number", axis=1).head(1)
    #print(f" Type of result: {type(largest_customer)}")

    return largest_customer
