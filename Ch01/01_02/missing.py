# %%
import pandas as pd
# test: try to commit

# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %%
df['amount'].astype('Int32')

# %%
df.isnull()

# %%
df.isnull().any(axis=1)

# %%
