# 47_leetcode#176_second_highest_salary
# Pandas solution 

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    df['rank'] = df['salary'].rank(method = 'dense', ascending = False)
    df = df[df['rank'] == 2]

    if len(df) >= 1:
        return df[['salary']].drop_duplicates().rename(columns = {'salary':'SecondHighestSalary'})
    else:
        return pd.DataFrame({'SecondHighestSalary': [float('nan')]})