import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

df = pd.read_parquet(clns)

# print(df.info())

# print(df["gameDate"].tail(50)) Data set starts 1951-11-11

