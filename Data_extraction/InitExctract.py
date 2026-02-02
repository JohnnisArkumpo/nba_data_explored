import pandas as pd

bs = '~/code/nba_data_explored/Data_extraction/PlayerStatistics.parquet'

df = pd.read_parquet(bs)

print(df.info())