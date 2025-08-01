# 18_leetcode#1633_percentage_of_users_attended_a_contest
# Pandas solution 

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(register, how = 'left', on = 'user_id')
    df = df.groupby('contest_id')['user_id'].count().reset_index(name = 'registered_count')

    user_count = len(users)
    df['percentage'] = ((df['registered_count'] / user_count)*100).round(2)

    return df[['contest_id','percentage']].sort_values(['percentage','contest_id'], ascending = [False, True])