# 21_leetcode#1174_immediate_food_delivery_ii
# Pandas solution 

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery
    df['is_immediate'] = 0
    mask_immediate = df['order_date'] == df['customer_pref_delivery_date']
    df.loc[mask_immediate, 'is_immediate'] = 1
    df['rank'] = df.sort_values(['customer_id','order_date']).groupby('customer_id').cumcount() + 1
    df = df[df['rank'] == 1]
    df = df.groupby('rank').agg({'is_immediate':'sum', 'delivery_id':'count'}).reset_index()
    df = df.rename(columns = {'is_immediate':'immediate_count', 'delivery_id':'delivery_count'})
    df['immediate_percentage'] = ((df['immediate_count'] / df['delivery_count'])*100).round(2)

    return df[['immediate_percentage']]