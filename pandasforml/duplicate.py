# analyzing duplicate data
import pandas as pd
data=pd.read_csv('data.csv')
print(data.duplicated())
# removing duplicate data
data.drop_duplicates(inplace=True)
print(data.to_string())
# checking the data frame after removing duplicate data
print(data.duplicated())