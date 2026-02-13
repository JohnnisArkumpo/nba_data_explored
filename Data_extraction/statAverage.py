import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'
st50 = '~/code/nba_data_explored/Data_extraction/nbaStats50s.parquet'
st60 = '~/code/nba_data_explored/Data_extraction/nbaStats60s.parquet'
st70 = '~/code/nba_data_explored/Data_extraction/nbaStats70s.parquet'
st80 = '~/code/nba_data_explored/Data_extraction/nbaStats80s.parquet'
st90 = '~/code/nba_data_explored/Data_extraction/nbaStats90s.parquet'
st2k = '~/code/nba_data_explored/Data_extraction/nbaStats2k.parquet'
st2k1 = '~/code/nba_data_explored/Data_extraction/nbaStats2k10.parquet'
st2k2 = '~/code/nba_data_explored/Data_extraction/nbaStats2k20.parquet'

# Take a single parquet file and find the statistical averages across the full file

df = pd.read_parquet(clns)

print(df.info())

# SELECT AVG(numMinutes, points, assists, blocks, steals, fieldGoalsAttempted, fieldGoalsMade, fieldGoalsPercentage, threePointersAttempted, threePointersMade, threePointersPercentage, freeThrowsPercentage, reboundsDefensive, reboundsOffensive, reboudsTotal, foulsPersonal, turnovers, plusMinusPoints)
# FROM df

# min = df.mean(df["numMinutes"])
# pnt = df["points"].mean()
# ast = df.mean(df["assists"])
# blk = df.mean("blocks")
# stl = df.mean("steals")
# fga = df.mean("fieldGoalsAttempted")
# fgm = df.mean("fieldGoalsMade")
# fgp = df.mean("fieldGoalsPercentage")
# tpa = df.mean("threePointersAttempted")
# tpm = df.mean("threePointersMade")
# tpp = df.mean("threePoiinterrsPercentage")
# fta = df.mean("freeThrowsAttempted")
# ftm = df.mean("freeThrowsMade")
# ftp = df.mean("freethrowsPercentage")
# rbd = df.mean("reboundsDefensive")
# rbo = df.mean("reboundsOffensive")
# rbt = df.mean(df["reboundsTotal"])
# flp = df.mean("foulsPersonal")
# trn = df.mean("turnovers")
# pmp = df.mean("plusMinusPoints")
# pnt = 1
ast = 2
rbt = 5

# print(f"In the 2000s players averaged {pnt} points, {ast} assists, and {rbt} rebounds.")

# debug timeee
# print(df['points'].isna().sum()) # 0? What the frick bro
# print(df['points'].head(2))