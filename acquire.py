import pandas as pd

def get_titanic():
    # Read titanic csv data
    df = pd.read_csv('titanic.csv')
    
    return df
