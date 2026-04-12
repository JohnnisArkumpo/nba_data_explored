import pandas as pd

dat = '~/code/nba_data_explored/Test_extractions/data.csv'

dMinus = pd.read_csv(dat)

print(f"{dMinus.info()}")

newd = dMinus.droplevel(0)

print(f"{newd.info()}")