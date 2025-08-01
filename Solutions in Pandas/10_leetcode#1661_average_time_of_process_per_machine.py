# 10_leetcode#1661_average_time_of_process_per_machine
# Pandas solution 

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.merge(activity, on = ('machine_id','process_id'), suffixes = ('_start','_end'))
    df = df[(df['activity_type_start'] == 'start') & (df['activity_type_end'] == 'end')][['machine_id','process_id','timestamp_start','timestamp_end']]
    df['processing_time'] = df['timestamp_end'] - df['timestamp_start']
    df = df.groupby('machine_id')[['processing_time']].mean().round(3).reset_index()
    return df