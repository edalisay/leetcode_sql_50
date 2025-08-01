# 38_leetcode#626_exchange_seats
# Pandas solution 

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    df = seat.sort_values('id')
    df['rank'] = df['id'].rank(method = 'first', ascending = False)
    df['next_id'] = df['id'].shift(-1)
    df['previous_id'] = df['id'].shift(1)
    df['new_id'] = None

    count_id = len(df)
    mask_odd = (df['id'] % 2 != 0) & (df['rank'] != 1)
    mask_evn = ((df['id'] % 2 == 0) & (df['rank'] != 1)) | ((df['rank'] == 1) & (count_id % 2 == 0))
    mask_lst = ((df['rank'] == 1) & (count_id % 2 != 0))

    df.loc[mask_odd, 'new_id'] = df['next_id']
    df.loc[mask_evn, 'new_id'] = df['previous_id']
    df.loc[mask_lst, 'new_id'] = df['id']
    
    df = df[['new_id','student']].rename(columns = {'new_id':'id'})
    return df.sort_values('id')