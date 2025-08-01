# 12_leetcode#1280_students_and_examinations
# Pandas solution 

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations.rename(columns = {'subject_name':'subject_name_x'}, inplace=True)

    df = students.merge(subjects, how = 'cross')
    df = df.merge(examinations, how = 'left', left_on = ('student_id','subject_name'), right_on = ('student_id','subject_name_x'))
    df = df.groupby(['student_id','student_name','subject_name'], dropna = False)['subject_name_x'].count()
    df = df.reset_index(name = 'attended_exams')

    # return df[df['student_name'] == 'Alice']
    return df