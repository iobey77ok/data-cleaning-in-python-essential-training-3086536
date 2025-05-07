# import sqlite
import sqlite3

#import invoke task
import pandas as pd
from invoke import task

#load and read
def load_csv(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['start', 'end'])
    return df

#validate
def validate(df):
    bad_time = df.query('start >= end')
    if len(bad_time) > 0:
        raise ValueError(bad_time)


@task
def etl(ctx, csv_file):
    df = load_csv(csv_file)
    validate(df)

    db_file = f'rides.db'
    #connect with sqlite
    conn = sqlite3.connect(db_file)

    df.to_sql('rides', conn, index=False, if_exists='append')
