# 30_leetcode#1731_the_number_of_employees_which_report_to_each_employee
# Pandas solution 

import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employees, left_on = 'employee_id', right_on = 'reports_to', suffixes = ('','_y'))
    df = df.groupby(['employee_id','name']).agg(
        reports_count = ('employee_id_y', 'count'),
        average_age = ('age_y', 'mean')
    ).reset_index()
    df['average_age'] = df['average_age'] + 1e-9
    return df.round()