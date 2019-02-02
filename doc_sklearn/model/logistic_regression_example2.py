#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(__doc__)

# Author wangzhefeng <wangzhefengr.@163.com>
# Computes path on IRIS dataset

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
from sklearn.svm import l1_min_c


# data
iris = datasets.load_iris()
train_x = iris.data
train_y = iris.target
train_x = train_x[train_y != 2]
train_x -= np.mean(a = train_x, axis = 0)
train_y = train_y[train_y != 2]

# train the model
cs = l1_min_c(train_x, train_y, loss = "log") * np.logspace(0, 3)

print("Computing regularization path ...")

start = datetime.now()

clf = linear_model.LogisticRegression(C = 1.0, penalty = "l1", tol = 1e-6)

coefs_ = []
for c in cs:
	clf.set_params(C = c)
	clf.fit(train_x, train_y)
	coefs_.append(clf.coef_.ravel().copy())

print("This took ", datetime.now() - start)


coefs_ = np.array(coefs_)
plt.plot(np.log10(cs), coefs_)
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()