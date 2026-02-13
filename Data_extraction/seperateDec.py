import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

df = pd.read_parquet(clns)

# print(df.info())

# print(df["gameDate"].tail(50)) Data set starts 1951-11-11

dcpath = '~/code/nba_data_explored/Data_extraction/nbaStats2k.parquet'
dcpathtwo = '~/code/nba_data_explored/Data_extraction/nbaStats2k10.parquet'
dcpaththree = '~/code/nba_data_explored/Data_extraction/nbaStats2k20.parquet'

df['gameDate'] = pd.to_datetime(df['gameDate'], format='%Y/%m/%d', errors='coerce')

# print(df['gameDate'].dtype)

decade = df[(df['gameDate'] >= '2000-01-01') & (df['gameDate'] < '2010-01-01')]
decade2 = df[(df['gameDate'] >= '2010-01-01') & (df['gameDate'] < '2020-01-01')]
decade3 = df[df['gameDate'] >= '2020-01-01']

decade.to_parquet(dcpath, index=False)
decade2.to_parquet(dcpathtwo, index=False)
decade3.to_parquet(dcpaththree, index=False)

# gameDate is before 1960-01-01 for the first query. Between required dates for each next one.

# somehow all of these files are empty? Tf did I do??