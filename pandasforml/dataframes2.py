# Locateb in data frame
# # locating in data frame
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar.loc[0])
# .loc[] is used to locate the data in the data frame with the help of index