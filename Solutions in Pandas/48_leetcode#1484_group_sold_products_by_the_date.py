# 48_leetcode#1484_group_sold_products_by_the_date
# Pandas solution 

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.sort_values(['sell_date','product']).drop_duplicates()
    df = df.groupby('sell_date').agg(
        num_sold = ('product','count'),
        products = ('product', lambda x: ','.join(x))
    ).reset_index()
    return df