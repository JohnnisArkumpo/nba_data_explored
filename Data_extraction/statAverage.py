import pandas as pd

clns = '~/code/nba_data_explored/Data_extraction/playerStatsClean.parquet'
st50 = '~/code/nba_data_explored/Data_extraction/nbaStats50.parquet'
st60 = '~/code/nba_data_explored/Data_extraction/nbaStats60.parquet'
st70 = '~/code/nba_data_explored/Data_extraction/nbaStats70.parquet'
st80 = '~/code/nba_data_explored/Data_extraction/nbaStats80.parquet'
st90 = '~/code/nba_data_explored/Data_extraction/nbaStats90.parquet'
st2k = '~/code/nba_data_explored/Data_extraction/nbaStats2k.parquet'
st2k10 = '~/code/nba_data_explored/Data_extraction/nbaStats2k10.parquet'
st2k20 = '~/code/nba_data_explored/Data_extraction/nbaStats2k20.parquet'

dec = "" # decade for string


# Function. This should be one that allows me to find the averages of any given decade.

def averages():
    print(f"")


df = pd.read_parquet(st2k20)

print(df.info())


# There should be a simpler way to do this, maybe using a dictionary filled out with all the statistical categories? Then they can be used to query.
# Basically the user would see "statistical categories are: 1. 2. etc"
# "Type the number for each statistical category you would like to include, then type 0 when you are finished"
# Then the program would loop and place the statistical categories in y=df[x].mean() or whatever function needed as many times as there were categories chosen.
min = df["numMinutes"].mean()
pnt = df["points"].mean()
ast = df["assists"].mean()
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
rbt = df["reboundsTotal"].mean()
# flp = df.mean("foulsPersonal")
# trn = df.mean("turnovers")
# pmp = df.mean("plusMinusPoints")

# print(f"In the 2020s players averaged {round(pnt, 1)} points, {round(ast, 1)} assists, and {round(rbt, 1)} rebounds.")

# debug timeee
# print(df['points'].isna().sum()) # 0? What the frick bro
# print(df['points'].head(2))