#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sklearn import linear_model

# data
train_x = [[0, 0], [1, 1]]
train_y = [0, 1]
test_x = [[1, 1]]

# model
reg = linear_model.Lasso(alpha = 0.1)
model = reg.fit(train_x, train_y)

print(model)
print(reg.coef_)
print(reg.intercept_)

# prediction
prediction = reg.predict(test_x)
print(prediction)


# linear_model.LassoCV()
# linear_model.LassoLarsCV()