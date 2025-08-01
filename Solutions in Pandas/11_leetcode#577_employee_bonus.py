# 11_leetcode#577_employee_bonus
# Pandas solution 

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, how = 'left', on ='empId')
    return df[(df['bonus'] < 1000) | (df['bonus'].isna())][['name','bonus']]