import pandas as pd

bs = '~/code/nba_data_explored/Data_extraction/PlayerStatistics.parquet'

df = pd.read_parquet(bs)

giannisGames = df.query('(firstName == Giannis)')

# I'm not sure if .query() works with strings or just with numbers, this may be my problem.

print(giannisGames.head(10))

# print(df.info())

