# This is day 2 of the Leetcode 30 Days of Panda.
# Link to problem description: 
# https://leetcode.com/problems/recyclable-and-low-fat-products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:

    selected = products[ (products.low_fats=='Y') & (products.recyclable=='Y')]

    return selected[ ['product_id']]
