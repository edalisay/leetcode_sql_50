# 08_leetcode#1581_customer_who_visited_but_did_not_make_any_transactions
# Pandas solution 

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, how = 'left', on = 'visit_id')[['customer_id','visit_id','transaction_id']]
    df = df[df['transaction_id'].isna()].groupby('customer_id').size().reset_index(name = 'count_no_trans')
    return df