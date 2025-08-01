# 40_leetcode#1321_restaurant_growth
# Pandas solution 

import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values('visited_on')
    df = df.groupby('visited_on')['amount'].sum().reset_index(name = 'daily_sum')
    df['amount'] = df['daily_sum'].rolling(window = 7, min_periods = 7).sum()
    df['average_amount'] = df['daily_sum'].rolling(window = 7, min_periods = 7).mean().round(2)
    return df[['visited_on','amount','average_amount']].dropna()