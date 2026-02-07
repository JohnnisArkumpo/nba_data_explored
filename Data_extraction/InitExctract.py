import pandas as pd

bs = '~/code/nba_data_explored/Data_extraction/PlayerStatistics.parquet'

df = pd.read_parquet(bs)

# giannisGames = df.query('(firstName == "Giannis")')

# I'm not sure if .query() works with strings or just with numbers, this may be my problem.
# .query() does in fact work with strings, but you need to use an extra set of quotes

# print(giannisGames.head(10))

print(df.info())

# We have a couple problems here. Firstly, games where a player does not play, it apppears they still have
# a recorded stat block. Because of the empty rebounds, steals, points, assists, etc. this will cause
# incorrect averages and skew the data. I need to find a way to avoid these missed games in the final totals. 
# I also currently have very good reason to believe that my computer will struggle heavily with this data set.
# Using the notebook files to query the data set resulted in VS code crashing twice, and simple queries like
# the one I just did finding the stats for Giannis's last 10 games took around 20 seconds to execute. I may
# not be able to complete this project as I do not have access to better machinery.


# I need to query enough just to understand the values in each column. 
# Once I have this done, my first step will be to write code to seperate by decade. 
# Then write code to find the average of all statistical categories for the entire NBA that decade
# I will also find a way in this ^ code to eliminate non-played games, probably by not including games with 0 minutes registered
# Then I will write code to isolate each player, using personId, and find their averages
# I will then write code that isolate the top 5 overall and top 3 players statistically at each position
# possibly finding the leaders in each statistical category as well. 
#### ^This is the primary objective. I can then find other ways to query the database and create good arguments as to who is better.
# I will attempt to find the average for teams each decade as well, to add that to seperate queries.


# Holy frick a chromebook was a bad idea.