#analyzing the data
#checking max value in the data frame
import pandas as pd 
data=pd.read_csv('data.csv')
print(data)
print(data.to_string())
print(data.max())
print(data.min())
print(data.head())
print(data.tail())
print(data.describe())
print(data.info())
