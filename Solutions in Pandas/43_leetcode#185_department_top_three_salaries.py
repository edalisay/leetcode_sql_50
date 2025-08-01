# 43_leetcode#185_department_top_three_salaries
# Pandas solution 

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, how = 'left', left_on = 'departmentId', right_on  = 'id')
    df = df.rename(columns = {'name_y':'Department','name_x':'Employee','salary':'Salary'})
    df['rank'] = df.groupby('Department')['Salary'].rank(method = 'dense', ascending = False)
    df = df[df['rank'] <= 3]
    return df[['Department','Employee','Salary']]
    # return df