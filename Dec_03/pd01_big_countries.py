# This is day 1 of the Leetcode 30 Days of Panda.
# Link to problem description: 
# https://leetcode.com/problems/big-countries/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    big = world[(world.area >= 3000000) | (world.population>=25000000)]
    big_countries = big[['name', 'population', 'area']]

    return big_countries
