#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这是一个文档注释'
__author__ = 'Alvin Wang'

print(__doc__)
print(__author__)
#=====================================================================
# 普通最小二乘回归(LS regression)
#=====================================================================

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

train_x = [[0, 0], [1, 1], [2, 2]]
train_y = [0, 1, 2]
test_x = [[1, 1], [3, 3,]]
reg = linear_model.LinearRegression()
# reg = linear_model.LinearRegression(fit_intercept = True, normalize = False, copy_X = True, n_jobs = 1)
model1 = reg.fit(train_x, train_y)
# reg.get_params(deep = True)
# reg.predict(X = test_x)
# reg.score()
# reg.set_params()
print(model1)
print(reg.coef_)
print(reg.intercept_)
