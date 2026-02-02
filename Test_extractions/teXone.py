import pandas as pd

cust = '~/code/nba_data_explored/Test_extractions/customers-100.csv'

firstDataSet = {
    'names': ["Giannis", "Khris", "Jrue", "P.J.", "Brook"],
    'positions': ["Power Forward", "Shooting Guard", "Point Guard", "Small Forward", "Center"]
}

lName = ["Antetokunmpo", "Middleton", "Holiday", "Tucker", "Lopez"]

firstTest = pd.DataFrame(firstDataSet)

secTest = pd.Series(lName,)

csvTest = pd.read_csv(cust)

print(csvTest.info())

