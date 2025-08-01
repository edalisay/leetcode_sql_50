# 27_leetcode#1729_find_followers_count
# Pandas solution 

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby('user_id')['follower_id'].count().reset_index(name = 'followers_count')
    return df