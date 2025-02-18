# cell with wrong format can make it difficult to analyze data
# to fix fix this issue either remove the row or replace the value with the correct format or convert into the correct format 
# Pandas has to_datetime()
import pandas as pd 
data=pd.read_csv('data.csv')
print(data)
print(data.to_string())
data['Date']=pd.to_datetime(data['Date'])

print(data.to_string())
# to remove the row with wrong format
for x in data.index:
    try:
        pd.to_datetime(data.loc[x,'Date'])
    except:
        data.drop(x,inplace=True)   
    
print(data.to_string())
# to replace the value with the correct format  
for x in data.index:
    try:
        pd.to_datetime(data.loc[x,'Date'])
    except:
        data.loc[x,'Date']='08-09-2021'
print(data.to_string())
