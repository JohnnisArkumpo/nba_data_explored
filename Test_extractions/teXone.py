import pandas as pd

pd.set_option('display.max_rows', None) # An attempt to see all values. Let's see how it goes

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

### I would like to mimic the experiment that I plan to do for my main project here. As a beginning point,
### I will find seperate groups of max pulse, ideally 5 different groups. I will then find the highest, lowest,
### and average amount of calories burned for each max pulse group. 

# print(dcn.loc[dcn["Maxpulse"] < 115, "Maxpulse"].sort_values(ascending=True))

mxp = dcn.query('(Maxpulse > 140) & (Maxpulse < 150)').sort_values("Calories", ascending=False)

print(mxp["Maxpulse"].sort_values(ascending=False))



# print(dc.info())