import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

df = pd.read_parquet(clns)

# print(df.info())

# print(df["gameDate"].tail(50)) Data set starts 1951-11-11

dcpath = '~/code/nba_data_explored/Data_extraction/nbaStats50s.parquet'

# gotta filter by date. I'm not sure how to do that as the date is in strings.

# df['gameDate'] = pd.to_datetime(df['gameDate'])

pd.to_datetime(df['gameDate'], errors='coerce', format='%Y/%m/%d', yearFirst=True)

# print(df.info)

decade = df.query('gameDate')

# decade.to_parquet(dcpath, index=False)

# gameDate is before 1960-01-01 for the first query. Between required dates for each next one.
