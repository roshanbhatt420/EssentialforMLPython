# rading data from the json file

import pandas as pd
df = pd.read_json('data.json')
print(df)
print(df.to_string()) # to_string() method is used to print the entire data frame
