# 50_leetcode#1517_find_users_with_valid_e-mails
# Pandas solution 

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df = df[df['mail'].str.contains(r'@leetcode\.com$', na=False)] 
    df = df[df['mail'].str.match(r'^[A-Za-z]', na=False)] 

    if len(df) < 1:
        return df
    else:
        edf = df['mail'].str.rpartition('@')
        return df[edf[0].str.match(r'^[A-Za-z0-9._-]+$', na=False)]