# 04_leetcode#1148_article_views_i
# Pandas solution 

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().rename(columns = {'author_id':'id'}).sort_values('id')