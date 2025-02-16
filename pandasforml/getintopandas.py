# series in pandas
# A series is a one-dimensional array that can hold any data type such as integers, floats, and strings
# A series can be created using various inputs like:
# Array
# Dict
# Scalar value or constant
# it just like a column in the table
# #creating a series from array

# creating a series from dict
import pandas as pd 
data={'a':0.,'b':1.,'c':2.}
var=pd.Series(data)
print(var)
# creating a series from scalar value
var=pd.Series(5,index=[0,1,2,3])
print(var)
# accessing data from series
print(var[0])
# creating a series from array
import numpy as np
data=np.array(['a','b','c','d'])
var=pd.Series(data)
print(var)
# creating a series from array with index
var=pd.Series(data,index=[100,101,102,103])
print(var)
# creating a series from array with index and name
var=pd.Series(data,index=[100,101,102,103],name='alphabets')
print(var)
