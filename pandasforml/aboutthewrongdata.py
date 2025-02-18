#wrong data does nor have empty cells it just have wrong data for expample date in wrong format 1999 instead of 1999-01-01
#  we can replpace the wrong data with the correct one
import pandas as pd
data=pd.read_csv('data.csv')
data.loc[7,'Date']='08-09-2021'
print(data.to_string())
