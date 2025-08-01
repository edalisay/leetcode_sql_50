# 33_leetcode#180_consecutive_numbers
# Pandas solution 

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs
    df['num-1'] = df['num'].shift(1)
    df['num-2'] = df['num'].shift(2)
    df = df[(df['num'] == df['num-1']) & (df['num'] == df['num-2'])]
    df = df[['num']].rename(columns = {'num':'ConsecutiveNums'}).drop_duplicates()
    return df