"""
Load traffic.csv into "traffic" table in sqlite3 database.

Drop and report invalid rows.
- ip should be valid IP (see ipaddress)
- time must not be in the future
- path can't be empty
- status code must be a valid HTTP status code (see http.HTTPStatus)
- size can't be negative or empty

Report the percentage of bad rows. Fail the ETL if there are more than 5% bad rows
"""
#%%
import pandas as pd

df = pd.read_csv('traffic.csv', parse_dates=['time'])
df
# %%
def is_valid_row(row):
    if row['time'] < pd.Timestamp('1900'):
        return False

    if pd.isnull(row['symbol']) or row['symbol'].strip() == '':
        return False

    if row['price'] <= 0:
        return False

    return True