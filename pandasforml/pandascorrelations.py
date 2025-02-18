#correlations in pandas
#correlation is a statistical measure that indicates the extent to which two or more variables fluctuate together.
# In other words, it is the statistical measure of the relationship between two variables.
# The correlation coefficient can range between -1 to +1.
# -1 indicates a strong negative correlation.
# +1 indicates a strong positive correlation.
# 0 indicates no correlation.
# The correlation coefficient is calculated using the formula:
# correlation = cov(X, Y) / (stdv(X) * stdv(Y))
# where X and Y are the variables for which we are calculating the correlation.
import pandas as pd
data=pd.read_csv('data.csv')
print(data.corr())
# The corr() method is used to calculate the correlation between the variables of the data frame.