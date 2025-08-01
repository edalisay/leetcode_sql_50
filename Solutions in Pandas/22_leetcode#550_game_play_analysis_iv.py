# 22_leetcode#550_game_play_analysis_iv
# Pandas solution 

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity
    df['rank'] = df.groupby('player_id')['event_date'].rank(method = 'first')
    df = df[df['rank'] < 3]
    df = df.sort_values(['player_id', 'event_date'])
    df['previous_event_date'] = df['event_date'].shift(1)
    df = df[(df['event_date'] - pd.Timedelta(days = 1) == df['previous_event_date']) & (df['rank'] == 2)]
    df = df[['player_id']].drop_duplicates()
    df['fraction'] = (df['player_id'].count() / len(activity[['player_id']].drop_duplicates())).round(2)

    if len(df) >= 1:
        return df[['fraction']].drop_duplicates()
    else:
        return pd.DataFrame({'fraction': [0]})