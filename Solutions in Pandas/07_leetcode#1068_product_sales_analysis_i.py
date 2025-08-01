# 07_leetcode#1068_product_sales_analysis_i
# Pandas solution 

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on = 'product_id')
    return df[['product_name','year','price']]