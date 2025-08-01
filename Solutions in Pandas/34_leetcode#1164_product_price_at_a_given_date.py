# 34_leetcode#1164_product_price_at_a_given_date
# Pandas solution 

import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    df = products.sort_values(['product_id','change_date'], ascending = [True, False])
    df = df[df['change_date'] <= '2019-08-16']
    df['rank'] = df.groupby('product_id')['change_date'].rank(method = 'first', ascending = False)
    df = df[df['rank'] == 1][['product_id','new_price']].rename(columns = {'new_price':'price'})

    # df2 = products[products['change_date'] > '2019-08-16']
    df2 = products
    df2['rank'] = df2.groupby('product_id')['change_date'].rank(method = 'first')
    df2 = df2[(df2['rank'] ==  1) & (df2['change_date'] > '2019-08-16')][['product_id']]
    df2['price'] = 10

    df = pd.concat([df, df2])
    # return df2[df2['product_id'] == 2]
    return df