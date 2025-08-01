# 09_leetcode#197_rising_temperature
# Pandas solution 

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values('recordDate')
    df['previousTemp'] = df['temperature'].shift(1)
    df['yesterDate'] = df['recordDate'].shift(1)
    df = df[(df['temperature'] > df['previousTemp']) & (df['recordDate'] == df['yesterDate'] + pd.Timedelta(days=1))]
    return df[['id']]