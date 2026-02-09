import pandas as pd

st50 = '~/code/nba_data_explored/Data_extraction/nbaStats50s.parquet'
st60 = '~/code/nba_data_explored/Data_extraction/nbaStats60s.parquet'
st70 = '~/code/nba_data_explored/Data_extraction/nbaStats70s.parquet'
st80 = '~/code/nba_data_explored/Data_extraction/nbaStats80s.parquet'
st90 = '~/code/nba_data_explored/Data_extraction/nbaStats90s.parquet'
st2k = '~/code/nba_data_explored/Data_extraction/nbaStats2k.parquet'
st2k1 = '~/code/nba_data_explored/Data_extraction/nbaStats2k10.parquet'
st2k2 = '~/code/nba_data_explored/Data_extraction/nbaStats2k20.parquet'

# Take a single parquet file and find the statistical averages across the full file

df = pd.read_parquet(st2k)

print(df.info())

# SELECT AVG(numMinutes, points, assists, blocks, steals, fieldGoalsAttempted, fieldGoalsMade, fieldGoalsPercentage, threePointersAttempted, threePointersMade, threePointersPercentage, freeThrowsPercentage, reboundsDefensive, reboundsOffensive, reboudsTotal, foulsPersonal, turnovers, plusMinusPoints)
# FROM df

