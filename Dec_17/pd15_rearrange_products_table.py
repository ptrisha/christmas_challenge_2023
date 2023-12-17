# Pandas problem Day 15
# Problem description:
# https://leetcode.com/problems/rearrange-products-table

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    df_melted = pd.melt(products, id_vars=["product_id"], value_vars=["store1", "store2", "store3"])

    #print(df_melted.columns)

    df_melted.dropna(inplace=True)

    df_melted.rename(columns={"value": "price", "variable": "store"}, inplace=True)

    return df_melted
