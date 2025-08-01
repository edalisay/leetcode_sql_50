# 42_leetcode#585_investments_in_2016
# Pandas solution 

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    df = insurance
    df['hasSameTIV15'] = df.groupby('tiv_2015')['pid'].transform('count')
    df['hasSameCity']  = df.groupby(['lat','lon'])['pid'].transform('count')

    df = df[(df['hasSameTIV15'] > 1) & (df['hasSameCity'] == 1)]
    sumTIV16 = ((df['tiv_2016'].astype(float).sum()) + 1e-9).round(2)
    return pd.DataFrame([sumTIV16], columns = ['tiv_2016'])