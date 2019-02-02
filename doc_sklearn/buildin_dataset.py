#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-11 15:37:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from sklearn import datasets

###################################################
#                   Datasets
###################################################
# iris (Classification)
iris = datasets.load_iris()
print(iris)
print(iris.data)
print(iris.data.shape)
print(iris.target)
print(iris.target.shape)
print(iris.feature_names)
print(iris.target_names)
print(iris.DESCR)

# digits (Classification)
digits = datasets.load_digits()
print(digits)
print(digits.data)
print(digits.data.shape)
print(digits.images)
print(digits.images.shape)
print(digits.target)
print(digits.target.shape)
print(digits.target_names)
print(digits.DESCR)

# boston (Regression)
boston = datasets.load_boston()
print(boston)
print(boston.data)
print(boston.data.shape)
print(boston.target)
print(boston.target.shape)
print(boston.feature_names)
print(boston.DESCR)

# diabetes (Regression)
diabetes = datasets.load_diabetes()
print(diabetes)
print(diabetes.data)
print(diabetes.data.shape)
print(diabetes.target)
print(diabetes.target.shape)

# linnerud (Multivariable Regression)
linnerud = datasets.load_linnerud()
print(linnerud)
print(linnerud.data)
print(linnerud.data.shape)
print(linnerud.target)
print(linnerud.target.shape)
print(linnerud.feature_names)
print(linnerud.target_names)
print(linnerud.DESCR)

#############################################
# Learning and predicting
#############################################




