# %%
import pandas as pd

csv_file = '2021-06.csv'

df = pd.read_csv(csv_file)
df
# %%
df['date'] = csv_file[:-len('.csv')]
df
# len('.csv') → 4
# csv_file[:-4] → slice the string 
# from the beginning up to but not 
# including the last 4 characters

# %%
times = df['time'].str.split('-', expand=True)
times.columns = ['start', 'end']
times
# %%
df = pd.concat([df, times], axis=1)
df

# %%
df['start'] = pd.to_datetime(
    df['date'].str.cat(df['start'], sep='T')
)
df['end'] = pd.to_datetime(
    df['date'].str.cat(df['end'], sep='T')
)
# sep=T 
#sep = separator
df

# %%
(df['end'] - df['start']).sum()

# %%
