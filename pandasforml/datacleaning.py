#Data cleaning is the process of preparing data for analysis by removing or modifying data that is incorrect, incomplete, irrelevant, duplicated, or improperly formatted. This data is usually not necessary or helpful when it comes to analyzing data because it may hinder the process or provide inaccurate results. Data cleaning is an essential part of the data analysis process, as it allows you to focus on the most relevant data and ensure that your results are accurate and reliable.
# bad data can be emppty cell ,data is wormg formated , wrong data , duplicate data , irrelevant data
# Data cleaning is an essential part of the data analysis process, as it allows you to focus on the most relevant data and ensure that your results are accurate and reliable.
# removal of empty cells
import pandas as pd
data=pd.read_csv('data.csv')
new_data=data.dropna()# remove the all rows with at least one missing value
print(new_data.to_string())
# replace empty values
import pandas as pd
data=pd.read_csv('data.csv')
data.fillna(130,inplace=True)
print(data.to_string())
# replace with mean value   

import pandas as pd
data=pd.read_csv('data.csv')
x=data['Calories'].mean()
data['Calories'].fillna(x,inplace=True)
print(data.to_string())
# replace with median value
import pandas as pd
data=pd.read_csv('data.csv')
x=data['Calories'].median()
data['Calories'].fillna(x,inplace=True)
print(data.to_string())
