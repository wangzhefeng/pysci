#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'这是一个文档注释'

__author__ = 'Alvin Wang'

print(__doc__)

#===========================================================
#                 linear_model example
#===========================================================
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# load the diabetes dataset
diabetes = datasets.load_diabetes()

# use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_y = diabetes.target

# split the data into training and testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# create linear regression object
regr = linear_model.LinearRegression()

# train the model using the training sets
model = regr.fit(diabetes_X_train, diabetes_y_train)

# make prediction using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

print('=' * 16 + 'Results' + '=' * 16)

# the coefficients and intercept
print('Coefficients:', regr.coef_)
print('Intercept:', regr.intercept_)
print('Prediction:', diabetes_y_pred)
# the mean squared error
print('Mean Squared Error: %.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

print('=' * 16 + 'Results' + '=' * 16)

# plot output
plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.plot(diabetes_X_test, diabetes_y_pred, color = 'blue', linewidth = 3)
plt.xticks(())
plt.yticks(())
plt.show()