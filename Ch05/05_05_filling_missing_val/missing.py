# %%
import pandas as pd


df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %% 
df['amount'].fillna(1, inplace=True)
# fill missing with 1
df

# %%
most_common = df['name'].mode()[0]
# pick the first one appear the most
df['name'].fillna(most_common, inplace=True)
df

# %%
df['date'].fillna(method='ffill', inplace=True)
df
# take the date from previous row 
# to fill the missing

# %%
import numpy as np
prices = df.groupby('name')['price'].transform(np.mean)
# group by name and select price col
# and find the mean of them
prices

# %%
df['price'].fillna(prices, inplace=True)
df
# %%
