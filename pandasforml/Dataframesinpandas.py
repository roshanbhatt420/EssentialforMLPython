# data frame are in pandas are two dimensional data structure
# it is like a table with rows and columns
# it is similar to the excel sheet

# creating a data frame from dict
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
# creating a data frame from dict with index
myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(myvar)
