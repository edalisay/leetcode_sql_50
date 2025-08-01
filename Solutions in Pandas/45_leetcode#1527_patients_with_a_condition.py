# 45_leetcode#1527_patients_with_a_condition
# Pandas solution 

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients[(patients['conditions'].str.contains(' DIAB1')) | (patients['conditions'].str.startswith('DIAB1'))]
    return patients