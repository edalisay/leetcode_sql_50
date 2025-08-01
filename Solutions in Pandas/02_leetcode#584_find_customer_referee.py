# 02_leetcode#584_find_customer_referee
# Pandas solution 

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())][['name']]