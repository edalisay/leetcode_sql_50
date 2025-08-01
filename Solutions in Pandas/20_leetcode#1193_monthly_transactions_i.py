# 20_leetcode#1193_monthly_transactions_i
# Pandas solution 

import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions
    df['month'] = df['trans_date'].dt.strftime('%Y-%m')
    df['approved_id'] = df.loc[df['state'] == 'approved', 'id']
    df['approved_amount'] = df.loc[df['state'] == 'approved', 'amount']
    df = df.groupby(['month','country'], dropna=False).agg(
        trans_count = ('id','count'),
        approved_count = ('approved_id', 'count'),
        trans_total_amount = ('amount', 'sum'),
        approved_total_amount = ('approved_amount','sum')
    ).reset_index()
    return df