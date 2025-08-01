# 23_leetcode#2356_number_of_unique_subjects_taught_by_each_teacher
# Pandas solution 

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher[['teacher_id','subject_id']].drop_duplicates()
    df = df.groupby('teacher_id')['subject_id'].count().reset_index(name = 'cnt')
    return df