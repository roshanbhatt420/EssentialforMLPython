#this is intoduction to the pandas
# Pandas is python library for data manipulation and analysis
# Pandas is built on top of NumPy
# It has functions for analyzing, cleaning, exploring, and manipulating data
# It is widely used in data science, machine learning, and data analysis
# Pandas references to the Panel data, which is an econometrics term for multidimensional structured data sets
# install pandas using "pip install pandas"
# impoting pandas
import pandas as pd
data={'Name':['Tom','Jerry','Mickey','Donald'],'Age':[20,21,22,23]}
var=pd.DataFrame(data)
# datafrome is a two-dimensional, size-mutable, heterogeneous tabular data
print(var)

# checking papndas version
print(pd.__version__)