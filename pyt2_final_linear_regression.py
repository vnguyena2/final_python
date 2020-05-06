import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

#builds a fuction that returns a predicted y, x1 and y1 are arrays
def predict_dependent(x1, y1, power):
    #reshape the x1 array to work for .fit()
    x1 = x1.reshape((-1,1))
    #determine a model type
    if power > 1 and power % 1 == 0:
        x1_ = PolynomialFeatures(degree=power, include_bias=False).fit_transform(x1)
        model = LinearRegression().fit(x1_, y1)
        prediction = model.predict(x1_)
    #linear is default
    else:
        model = LinearRegression().fit(x1,y1)
        prediction = model.predict(x1)
    return prediction

#scores how well the model fits that data with a R^2 score, with is from 0 to 1
def prediction_score(x1, y1, power):
    x1 = x1.reshape((-1,1))
    if power > 1 and power % 1 == 0:
        x1_ = PolynomialFeatures(degree=power, include_bias=False).fit_transform(x1)
        model = LinearRegression().fit(x1_, y1)
        score = model.score(x1_, y1)
    else:
        model = LinearRegression().fit(x1,y1)
        score = model.score(x1, y1)
    return score
#take in a set and return a set with the same x but new predicted y
def regression_transform_linear(x1, y1):
    #build a model
    x2 = x1
    np.sort(x2)
    x1 = x1.reshape((-1,1))
    model = LinearRegression().fit(x1,y1)
    x3 = x1
    np.sort(x3)
    y2 = model.predict(x3)
    set_rebuild = pd.Series(y2, index = x2)
    #use the model to build a dataset
    return set_rebuild



x = np.array([5, 15, 25, 35, 45, 55])
y = np.array([5, 20, 14, 32, 22, 38])
print(predict_dependent(x,y,1))
print(prediction_score(x,y,1))
print(predict_dependent(x,y,2))
print(prediction_score(x,y,2))
print(predict_dependent(x,y,3))
print(prediction_score(x,y,3))
print(regression_transform_linear(x, y))
regression_transform_linear(x, y).plot()
