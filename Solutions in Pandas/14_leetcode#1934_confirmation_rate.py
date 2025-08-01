# 14_leetcode#1934_confirmation_rate
# Pandas solution 

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations, how = 'left', on = 'user_id')
    df = df.rename(columns = {'time_stamp_x':'sign_up_time', 'time_stamp_y':'time_stamp'})

    df['is_confirmed'] = df['action'].map({'confirmed': 1, 'timeout': 0}).fillna(0).astype(int)
    df = df[['user_id','action','is_confirmed']]
    df = df.groupby('user_id')['is_confirmed'].agg(['sum', 'count']).reset_index()

    df['confirmation_rate'] = (df['sum'] / df['count']).round(2)
    return df[['user_id','confirmation_rate']]