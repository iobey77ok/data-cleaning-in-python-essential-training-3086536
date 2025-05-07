# %%
import pandas as pd

df = pd.read_csv('points.csv')
df.dtypes
# pandas will predict the field if we
# don't specify
# %%
def asint(val):
    return int(val, base=0)
# base=0 meaning get the base from string
# the color now start with 0
# so it will convert to base 16 int

df['color'] = df['color'].apply(asint)
df.dtypes

# %%
bools = {
    'yes': True,
    'no': False,
}
df['visible'] = df['visible'].map(bools)
df.dtypes

# %%
df