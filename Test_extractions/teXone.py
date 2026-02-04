import pandas as pd

cust = '~/code/nba_data_explored/Test_extractions/customers-100.csv'

dat = '~/code/nba_data_explored/Test_extractions/data.csv'

firstDataSet = {
    'names': ["Giannis", "Khris", "Jrue", "P.J.", "Brook"],
    'positions': ["Power Forward", "Shooting Guard", "Point Guard", "Small Forward", "Center"]
}

lName = ["Antetokunmpo", "Middleton", "Holiday", "Tucker", "Lopez"]

firstTest = pd.DataFrame(firstDataSet)

secTest = pd.Series(lName,)

csvTest = pd.read_csv(cust)

newTest = csvTest.dropna

dc = pd.read_csv(dat)

dcn = dc.dropna()

# print(csvTest.info())

# print(dc.corr())

### Alright so we're gonna work on finding the highest calorie burn in data.csv, but we're going to get the top 
### three results for each range of max calories. We are going to begin by querying and finding out what
### the range of max pulse is. 

# SQL code here: SELECT calories FROM dc ORDER BY calories DESC

# SQL for the max pulse query: SELECT maxpulse FROM dc ORDER BY maxpulse DESC

# print(dcn.loc[dcn["Calories"] > 0, "Maxpulse"].sort_values(ascending=False))

### Just need to change the amount of results allowed now.

# print(dc.info())