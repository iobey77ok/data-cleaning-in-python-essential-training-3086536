# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0
df.dtypes
# %%
# check for null
null_check = df.isnull().any(axis=1)
df[null_check]
# %%
check_plate = ~df['plate'].str.match(r'^[0-9A-Z]{3,}', na=False)
df[check_plate]
# %%
check_distance = df['distance'] < 0
check_distance
# %%
filter_out = null_check | check_plate | check_distance
df[filter_out]
# %%
