# DATA CLEANING AND MACHINE LEARNING 
#HOW To store the data into the dataframes 
import pandas as pd 
import sklearn
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version=1, as_frame=True)
df.info()