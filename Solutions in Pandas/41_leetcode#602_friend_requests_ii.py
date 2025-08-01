# 41_leetcode#602_friend_requests_ii
# Pandas solution 

import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df1 = request_accepted.rename(columns = {'requester_id':'id','accepter_id':'friends_id'})
    df2 = request_accepted.rename(columns = {'accepter_id':'id','requester_id':'friends_id'})
    df  = pd.concat([df1, df2])[['id','friends_id']].drop_duplicates()
    df  = df.groupby('id')['friends_id'].count().reset_index(name = 'num').sort_values('num', ascending = False)
    return df.head(1)