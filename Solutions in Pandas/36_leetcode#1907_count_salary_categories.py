# 36_leetcode#1907_count_salary_categories
# Pandas solution 

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    mask_low = accounts['income'] < 20000
    mask_ave = accounts['income'].between(20000, 50000)
    mask_hi  = accounts['income'] > 50000

    df = accounts
    df['category'] = 'Low Salary'
    df.loc[mask_ave, 'category'] = 'Average Salary'
    df.loc[mask_hi , 'category'] = 'High Salary'

    categories = pd.DataFrame(['Low Salary','Average Salary','High Salary'], columns = ['category'])
    df = df.merge(categories, how = 'right', on = 'category')
    df = df.groupby('category')['account_id'].count().reset_index(name = 'accounts_count')

    return df