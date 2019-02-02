#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这是一个文档注释'

__author__ = 'Tinker Wang'

# import builtins
# import os
# import sys
# from collections import Iterable
# import keyword
# import random
# from functools import reduce
import numpy as np
# import numpy.random
# import numpy.linalg
# import pandas as pd
# from pandas import Series, DataFrame
# import matplotlib.pyplot as plt
# import seaborn as sns
# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# from urllib.request import urlopen
# import urllib.error
# from urllib.error import HTTPError, URLError
# import urllib.parse
# import urllib.robotparser
# import re
# import json
# import heapq
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC, LinearSVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

#===============================================================
#   An introduction to machine learning with scikit-learn
#===============================================================

from sklearn import datasets
from sklearn import svm
import pickle
from sklearn.externals import joblib
from sklearn import random_projection
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer




#================================================================
#                 Loading an example dataset
#================================================================
iris = datasets.load_iris()
# print(iris)
# print(iris.data)
# print(iris.target)
# print(iris.target_names()
digits = datasets.load_digits()
# print(digits)
# print('--------------------------------------------')
# print(digits.data)
# print(digits.data.ndim)
# print(digits.data.shape)
# print('--------------------------------------------')
# print(digits.target)
# print(digits.target.ndim)
# print(digits.target.shape)
# print('--------------------------------------------')
# print(digits.images)
# print(digits.images.ndim)
# print(digits.images.shape)

#================================================================
#                 Learning and predicting
#================================================================
clf_digits = svm.SVC(gamma = 0.01, C = 100.0)

# dataset
train_data_digits = digits.data[:-1]
train_target_digits = digits.target[:-1]
test_data_digits = digits.data[-1:]
test_target_digits = digits.target[-1:]

# learning and predicting 
model_digits = clf_digits.fit(train_data_digits, train_target_digits)
print(model_digits)
print(clf_digits.gamma)
# print(clf_digits.estimated_param_)
print(clf_digits.C)
prediction_digits = clf_digits.predict(test_data_digits)
print(prediction_digits)
print(prediction_digits == test_target_digits)
#================================================================
#                 Model persistence
#================================================================
clf_iris = svm.SVC()

# train dataset
train_data_iris, train_target_iris = iris.data[3:], iris.target[3:]
train_data_iris2, train_target_iris2 = iris.data[3:], iris.target_names[iris.target[3:]]
# test dataset
test_data_iris, test_target_iris = iris.data[:3], iris.target[:3]
test_data_iris2, test_target_iris2 = iris.data[:3], iris.target_names[iris.target[:3]]

# learning and predicting
model_iris = clf_iris.fit(train_data_iris, train_target_iris)
print(model_iris)

s = pickle.dumps(clf_iris)
clf_iris2 = pickle.loads(s)
prediction_iris = clf_iris2.predict(test_data_iris)
print(list(prediction_iris))
print(prediction_iris == test_target_iris)

# another pickle method
joblib.dump(clf_iris, 'iris_training.pkl')
clf_iris3 = joblib.load('iris_training.pkl')
prediction_iris2 = clf_iris3.predict(test_data_iris)
print(prediction_iris2)
print(prediction_iris2 == test_target_iris)

print('---------------------------------------------------------------------')
clf_iris = svm.SVC()

model_iris2 = clf_iris.fit(train_data_iris2, train_target_iris2)
print(model_iris2)

prediction_iris3 = clf_iris.predict(test_data_iris2)
print(list(prediction_iris3))
print(prediction_iris3 == test_target_iris2)

#================================================================
#                          Conventions
#================================================================
rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
print(X)
X = np.array(X, dtype = 'float32')
print(X)
print(X.ndim)
print(X.shape)
print(X.dtype)

transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new)
print(X_new.dtype)
#================================================================
#                  Refitting and updating parameters
#================================================================
rng = np.random.RandomState(0)
X = rng.rand(100, 10)
print(X)
y = rng.binomial(1, 0.5, 100)
print(y)
X_test = rng.rand(5, 10)
print(X_test)

clf = svm.SVC()

model1 = clf.set_params(kernel = 'linear').fit(X, y)
print(model1)
prediction1 = clf.predict(X_test)
print(prediction1)

model2 = clf.set_params(kernel = 'rbf').fit(X, y)
print(model2)
prediction2 = clf.predict(X_test)
print(prediction2)
#================================================================
#                  Multiclass vs. multilabel fitting
#================================================================
X = [[1, 2]
     [2, 4],
     [4, 5],
     [3, 2],
     [3, 1]]
y = [0, 0, 1, 1, 2]
classif = OneVsRestClassifier(estimator = svm.SVC(random_state = 0))
model_multiclass = classif.fit(X, y).predict(X)
print(model_multiclass)


y = LabelBinarizer().fit_transform(y)
print(y)
model_multiclass2 = classif.fit(X, y).predict(X)
print(model_multiclass2)


y = [[0, 1],
	 [0, 2],
	 [1, 3],
	 [0, 2, 3],
	 [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
print(y)
model_multiclass3 = classif.fit(X, y).predict(X)
print(model_multiclass3)

