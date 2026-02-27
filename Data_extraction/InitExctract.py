import pandas as pd

bs = '~/code/nba_data_explored/Data_extraction/PlayerStatistics.parquet'

df = pd.read_parquet(bs)

gp = df.query('numMinutes > 0')

path_to_np = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'

gp.to_parquet(path_to_np, index=False)

# Simply clearing out the rows where there was an inactive player