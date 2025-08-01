# 44_leetcode#1667_fix_names_in_a_table
# Pandas solution 

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')