# 25_leetcode#1070_product_sales_analysis_iii
# Pandas solution 

import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales
    df['rank'] = df.groupby('product_id')['year'].rank(method = 'average')
    df = df[df['rank'] < 2].rename(columns = {'year':'first_year'})
    return df[['product_id','first_year','quantity','price']]
    # return df[df['product_id'] == 1]