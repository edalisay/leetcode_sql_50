# 37_leetcode#1978_employees_whose_manager_left_the_company
# Pandas solution 

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[(employees['salary'] < 30000) & (~employees['manager_id'].isna())]
    df = df.merge(employees, how = 'left', left_on = 'manager_id', right_on = 'employee_id')
    df = df[df['employee_id_y'].isna()][['employee_id_x']]
    df = df.rename(columns = {'employee_id_x':'employee_id'}).sort_values('employee_id')
    return df