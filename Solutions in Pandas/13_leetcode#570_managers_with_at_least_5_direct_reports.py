# 13_leetcode#570_managers_with_at_least_5_direct_reports
# Pandas solution 

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId')['id'].count().reset_index(name = 'directCount')
    df = employee.merge(df, how = 'left', left_on = 'id', right_on = 'managerId')
    df = df[df['directCount'] >= 5]
    return df[['name']]