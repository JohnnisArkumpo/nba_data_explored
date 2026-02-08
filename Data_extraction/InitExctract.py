import pandas as pd

bs = '~/code/nba_data_explored/Data_extraction/PlayerStatistics.parquet'

df = pd.read_parquet(bs)

gp = df.query('numMinutes > 0')

# print(gp.head(5))

# gotta create a new file

path_to_np = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

gp.to_parquet(path_to_np, index=False)

# print(df.info())

# Holy frick a chromebook was a bad idea.

#### Just gonna leave this file. Starting with a clean file now so I can leave the failed processes in the past