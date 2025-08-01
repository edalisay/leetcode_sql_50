# 49_leetcode#1327_list_the_products_ordered_in_a_period
# Pandas solution 

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(products, how = 'left', on = 'product_id')
    df = df[df['order_date'].dt.strftime('%Y-%m') == '2020-02']
    df = df.groupby('product_name')['unit'].sum().reset_index()
    return df[df['unit'] >= 100]