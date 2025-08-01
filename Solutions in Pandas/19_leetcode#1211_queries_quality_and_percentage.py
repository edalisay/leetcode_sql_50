# 19_leetcode#1211_queries_quality_and_percentage
# Pandas solution 

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries
    df['quality'] = df['rating'] / df['position']
    df['is_poor_rating'] = 0
    mask_rating = df['rating'] < 3

    df.loc[mask_rating, 'is_poor_rating'] = 1
    df = df.groupby('query_name').agg({'rating':'count','quality':'mean','is_poor_rating':'sum'}).reset_index()
    df['quality'] = df['quality'] + 1e-9
    df['poor_query_percentage'] = (df['is_poor_rating'] / df['rating'])*100
    df = df[~df['query_name'].isnull()]
    return df[['query_name','quality','poor_query_percentage']].round(2).sort_values('query_name')
    # return df[df['query_name'] == 'szsgysmafhfhstnagzhryxykvkmzn'][['query_name','quality','poor_query_percentage']].round(2).sort_values('query_name')
    