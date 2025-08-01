# 28_leetcode#619_biggest_single_number
# Pandas solution 

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers
    df['rank'] = df.groupby('num')['num'].rank(method = 'first')
    df = df.groupby('num')['rank'].count().reset_index(name = 'count').sort_values('num', ascending = False)
    df = df[df['count'] == 1]

    if len(df) >= 1:
        return df.head(1)[['num']]
    else:
        return pd.DataFrame({'num': [float('nan')]})