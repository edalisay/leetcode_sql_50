# 29_leetcode#1045_customers_who_bought_all_products
# Pandas solution 

import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    all_products = len(product.drop_duplicates())
    df = customer[['customer_id','product_key']].drop_duplicates()
    df = df.groupby('customer_id')['product_key'].count().reset_index(name = 'product_bought')
    df = df[df['product_bought'] == all_products]
    return df[['customer_id']]