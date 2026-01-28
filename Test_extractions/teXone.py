import pandas as pd

#cust = ~/code/nba_data_explored/Test_extractions/customers-100.csv

df = pd.DataFrame('~/code/nba_data_explored/Test_extractions/customers-100.csv')
# pd.read_csv(cust)

# print(df.to_string())

print(df.loc[0])