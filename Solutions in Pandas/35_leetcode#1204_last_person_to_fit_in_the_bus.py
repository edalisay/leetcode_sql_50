# 35_leetcode#1204_last_person_to_fit_in_the_bus
# Pandas solution 

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.sort_values('turn')
    df['cumsum'] = df['weight'].cumsum()
    df = df[df['cumsum'] <= 1000]
    return df.tail(1)[['person_name']]