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

# M>139: 48, 140>M>128: 60, 129>M>118: 49, 119>M: 15. 4 Groups of max pulse that will be used for next step.

mxp1 = dcn.query('(Maxpulse > 139)') #  Highest calories burned for the M>139 group
mxp2 = dcn.query('(Maxpulse < 140) & (Maxpulse > 128)') # Ditto, between 140-128
mxp3 = dcn.query('(Maxpulse < 129) & (Maxpulse > 118)') # " " 129-118
mxp4 = dcn.query('(Maxpulse < 119)') # " " 119-

print("Maximum calories consumed with a max pulse of 140+ ")
print(mxp1["Calories"].max())

print("Maximum calories consumed with a max pulse of 129-139 ")
print(mxp2["Calories"].max())

print("Maximum calories consumed with a max pulse of 119-128 " )
print(mxp3["Calories"].max())

print("Maximum calories consumed with a max pulse of 118- ")
print(mxp4["Calories"].max())

# Lowest calories for each group

print("Minimum for group 1")
print(mxp1["Calories"].min())

print("Minimum for group 2")
print(mxp2["Calories"].min())

print("Minimum for group 3")
print(mxp3["Calories"].min())

print("Minimum for group 4")
print(mxp4["Calories"].min())

# Average calories for each group

print("Average for group 1")
print(mxp1["Calories"].mean())

print("Average for group 2")
print(mxp2["Calories"].mean())

print("Average for group 3")
print(mxp3["Calories"].mean())

print("Average for group 4")
print(mxp4["Calories"].mean())