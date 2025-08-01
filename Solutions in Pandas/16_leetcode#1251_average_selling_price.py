# 16_leetcode#1251_average_selling_price
# Pandas solution 

import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = units_sold.merge(prices, how = 'right', on = 'product_id')
    df = df[(df['purchase_date'].between(df['start_date'], df['end_date'])) | (df['units'].isnull())]
    df['total_price'] = df['units'] * df['price']
    df = df.groupby('product_id')[['units','total_price']].sum().reset_index()
    df['average_price'] = 0

    mask_units = df['units'] > 0
    df.loc[mask_units, 'average_price'] = (df['total_price'] / df['units']).round(2)
    return df[['product_id','average_price']]