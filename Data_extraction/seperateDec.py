import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

df = pd.read_parquet(clns)


# print(df["gameDate"].tail(50)) Data set starts 1951-11-11

dcpath = '~/code/nba_data_explored/Data_extraction/nbaStats50.parquet'

df['gameDate'] = pd.to_datetime(df['gameDate'], format='ISO8601', utc=True, errors='coerce').dt.tz_localize(None)

decade = df[(df['gameDate'] < '1960-01-01')]

# print(df.info())

print(decade.head(25))

# decade.to_parquet(dcpath, index=False)

# gameDate is before 1960-01-01 for the first query. Between required dates for each next one.

# somehow all of these files are empty? Tf did I do??
# I got it finally.