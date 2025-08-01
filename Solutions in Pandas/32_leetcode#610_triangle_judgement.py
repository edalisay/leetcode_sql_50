# 32_leetcode#610_triangle_judgement
# Pandas solution 

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = triangle
    df['triangle'] = 'No'

    mask_triangle = ((abs(df['x']) + abs(df['y']) > abs(df['z'])) 
                    & (abs(df['x']) + abs(df['z']) > abs(df['y'])) 
                    & (abs(df['y']) + abs(df['z']) > abs(df['x'])))

    df.loc[mask_triangle, 'triangle'] = 'Yes'
    return df