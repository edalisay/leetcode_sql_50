# 31_leetcode#1789_primary_department_for_each_employee
# Pandas solution 

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    df['dept_count'] = df.groupby('employee_id')['department_id'].transform('count')
    mask_primary = df['dept_count'] == 1
    df.loc[mask_primary, 'primary_flag'] = 'Y'
    return df[df['primary_flag'] == 'Y'][['employee_id','department_id']]