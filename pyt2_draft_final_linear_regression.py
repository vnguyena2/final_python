import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#builds a fuction that returns a predicted y, x1 and y1 are arrays
def predict_dependent(x , x1, y1, power):
    #reformates one of the arrays so .fit() works
    x1 = x1.reshape((-1,1))
    #determines witch type of fucntion is used
    if power == 1:
        model = LinearRegression().fit(x1,y1)
    elif power > 1 and power % 1 == 0:
        x1_ = PolynomialFeatures(degree=power, include_bias=False).fit_transform(x1)
        model = LinearRegression().fit(x1_, y1)
    prediction = model.predict(x)
    return prediction

#scores how well the model fits that data with a R^2 score, witch is from 0 to 1
def prediction_score(x1, y1, power):
    x1 = x1.reshape((-1,1))
    if power == 1:
        model = LinearRegression().fit(x1,y1)
        score = model.score(x1, y1)
    elif power > 1 and power % 1 == 0:
        x1_ = PolynomialFeatures(degree=power, include_bias=False).fit_transform(x1)
        model = LinearRegression().fit(x1_, y1)
        score = model.score(x1_, y1)
    return score
'''    
#take in a set and return a set with the same x but new predicted y
def regression_transform(set_prebulid, power):
    return set_rebulid
    #note- imcomplte
'''
x = np.array([5, 15, 25, 35, 45, 55])
y = np.array([5, 20, 14, 32, 22, 38])
print(predict_dependent(4, x, y, 1))
