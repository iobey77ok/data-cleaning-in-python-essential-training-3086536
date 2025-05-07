# %%
import pandas as pd

df = pd.read_csv('weather.csv', parse_dates=['DATE'])
df
# parse_dates=['DATE']: Tells Pandas to convert the 'DATE' 
# column to datetime format (datetime64[ns]) 
# instead of keeping it as a string.
# %%
df.rename(columns={
    'DATE': 'date',
    'TMIN': 'min_temp',
    'TMAX': 'max_temp',
}, inplace=True)
# tells Pandas to modify the DataFrame directly 
# not returning a new one.
df
# %%
df = pd.read_csv('donations.csv')
df
# %%
import re


def fix_col(col):
    """Fix column name
    >>> fix_col('1. First Name')
    'first_name'
    """
    return (
        re.sub(r'\d+\.\s+', '', col)
        .lower()
        .replace(' ', '_')
    )
# Uses regular expression to remove leading 
# numbers followed by a dot and space.
df.rename(columns=fix_col, inplace=True)
df
# %%
