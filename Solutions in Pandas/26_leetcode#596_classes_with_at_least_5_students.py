# 26_leetcode#596_classes_with_at_least_5_students
# Pandas solution 

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    df = df[df['student'] >= 5]
    return df[['class']]