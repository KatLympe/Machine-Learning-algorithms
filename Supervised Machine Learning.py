%Project part of the "Applied Machine Learning in Python" course (Module 2) from University of Michigan and Coursera. 


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10


X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

# Q: Create a function that fits a polynomial LinearRegression model on the training data X_train for degrees 1, 3, 6, and 9. 
# (Use PolynomialFeatures in sklearn.preprocessing to create the polynomial features and then fit a linear regression model) 
# For each model, find 100 predicted values over the interval x = 0 to 10 (e.g. np.linspace(0,10,100)) and store this in a numpy array. 
# The first row of this array should correspond to the output from the model trained on degree 1, the second row degree 3, the third row degree 6, 
# and the fourth row degree 9.


def answer_one():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    
    predict = np.linspace(0,10,100).reshape(100, 1)
    X_train_reshaped = X_train.reshape(X_train.size, 1)

    poly = PolynomialFeatures(degree=1)
    X_polynom_1 = poly.fit_transform(X_train_reshaped)
    y_polynom_1 = poly.fit_transform(predict)
    linreg1 = LinearRegression().fit(X_poly1, y_train)
    array1 = linreg1.predict(y_poly1)
    
    poly = PolynomialFeatures(degree=3)
    X_polynom_3 = poly.fit_transform(X_train_reshaped)
    y_polynom_3 = poly.fit_transform(predict)
    linreg3 = LinearRegression().fit(X_poly3, y_train)
    array3 = linreg3.predict(y_poly3)
    
    poly = PolynomialFeatures(degree=6)
    X_polynom_6 = poly.fit_transform(X_train_reshaped)
    y_polynom_6 = poly.fit_transform(predict)
    linreg6 = LinearRegression().fit(X_poly6, y_train)
    array6 = linreg6.predict(y_poly6)
    
    poly = PolynomialFeatures(degree=9)
    X_polynom_9 = poly.fit_transform(X_train_reshaped)
    y_polynom_9 = poly.fit_transform(predict)
    linreg9 = LinearRegression().fit(X_poly9, y_train)
    array9 = linreg9.predict(y_poly9)
    
    return np.vstack((array1, array3, array6, array9))



#Question 2
#Write a function that fits a polynomial LinearRegression model on the training data X_train for degrees 0 through 9. For each model compute the  R2 
#(coefficient of determination) regression score on the training data as well as the the test data, and return both of these arrays in a tuple.
#This function should return one tuple of numpy arrays (r2_train, r2_test). Both arrays should have shape (10,)


def answer_two():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.metrics.regression import r2_score

    # Your code here
    results_train = np.zeros([10, 1])
    results_test = np.zeros([10, 1])

    
    for i in range(0,10):
        
        poly = PolynomialFeatures(degree=i)
        X_train_poly = poly.fit_transform(X_train.reshape(-1, 1)) 
        X_test_poly = poly.fit_transform(X_test.reshape(-1, 1))
        linreg = LinearRegression().fit(X_train_poly, y_train)

        # Get the score
        score_train = r2_score( y_train,linreg.predict(X_train_poly))
        score_test = r2_score( y_test,linreg.predict(X_test_poly))
        
        #Results
        res_train[i] = score_train
        res_test[i] = score_test
        
        res_train = results_train.flatten()
        res_test = results_test.flatten()
    
    answer = (results_train, results_test)

    return (results_train, results_test)

answer_two()

# Code mainly inspired by TSG405 and amirkeren
