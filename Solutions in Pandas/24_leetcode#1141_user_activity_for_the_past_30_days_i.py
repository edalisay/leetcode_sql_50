# 24_leetcode#1141_user_activity_for_the_past_30_days_i
# Pandas solution 

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df = df[df['activity_date'].between((pd.to_datetime('2019-07-27') - pd.Timedelta(days = 29)), pd.to_datetime('2019-07-27'))]
    df = df[['activity_date','user_id']].drop_duplicates()
    df = df.groupby('activity_date')['user_id'].count().reset_index()
    return df.rename(columns = {'activity_date':'day','user_id':'active_users'})