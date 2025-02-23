# visual thr machine learnng methododlogy 
# first we create the model and second feed the data 
import sklearn 
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
# model is created 
from sklearn.linear_model import LinearRegression
model=LinearRegression()
# we have to feed the data to the model
model.fit(X,y)
# best thimg is that API is also same for all model
#We want to model differen than 
from sklearn.neighbors import KNeighborsRegressor
model=KNeighborsRegressor()
model.predict(X)

