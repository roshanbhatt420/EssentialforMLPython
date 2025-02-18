# reading the data from the csv file
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df.to_string()) # to_string() method is used to print the entire data frame
# The read_csv() method is used to read the data from the csv file and convert it
# checking max value in the data frame
print(df.max())
# checking min value in the data frame
print(df.min())
# checking mean value in the data frame
print(df.mean())