# 39_leetcode#1341_movie_rating
# Pandas solution 

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df = movie_rating.merge(users, how = 'left', on = 'user_id')
    df = df.groupby(['user_id','name'])['rating'].count().reset_index(name = 'count')
    df = df.sort_values(['count','name'], ascending = [False, True])
    results1 = df.head(1)[['name']].rename(columns = {'name':'results'})

    df = movie_rating.merge(movies, how = 'left', on = 'movie_id')
    df = df[df['created_at'].dt.strftime('%Y-%m') == '2020-02']
    df = df.groupby(['movie_id','title'])['rating'].mean().reset_index(name = 'average')
    df = df.sort_values(['average','title'], ascending = [False, True])
    results2 = df.head(1)[['title']].rename(columns = {'title':'results'})

    df = pd.concat([results1, results2])
    return df