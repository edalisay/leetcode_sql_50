# 46_leetcode#196_delete_duplicate_emails
# Pandas solution 

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace = True)
    person.drop_duplicates(subset=['email'], inplace=True)
    return