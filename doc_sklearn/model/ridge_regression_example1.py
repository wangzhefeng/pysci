#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
文档注释
'''

__author__ = "wangzhefeng"

print(__doc__)
print(__author__)


# plot ridge coefficients as a function of the regularization


import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# data
train_x = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
train_y = np.ones(10)

# compute paths
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
	ridge = linear_model.Ridge(alpha = a, fit_intercept = False)
	ridge.fit(train_x, train_y)
	coefs.append(ridge.coef_)

# result
print(alphas)
print(coefs)

# display result
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])
plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("Ridge coefficients as a function of the regularization")
plt.axis("tight")

plt.show()