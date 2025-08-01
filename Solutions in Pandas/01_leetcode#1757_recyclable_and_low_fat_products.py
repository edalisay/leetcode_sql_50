# 01_leetcode#1757_recyclable_and_low_fat_products
# Pandas solution 

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']]