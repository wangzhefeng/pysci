#!/usr/bin/env python3# -*- coding: utf-8 -*-'这是一个文档注释'__author__ = 'Tinker Wang'import numpy as npfrom sklearn import linear_modelfrom sklearn import svmfrom sklearn import datasets#===========================================================#          Linear model: from regression to sparsity#===========================================================diabetes = datasets.load_diabetes()print(diabetes)print(diabetes.data)print(diabetes.data.shape)print(diabetes.target)print(diabetes.target.shape)diabetes_X_train =diabetes.data[:-20]diabetes_y_train = diabetes.target[:-20]diabetes_X_test = diabetes.data[-20:]diabetes_y_test = diabetes.target[-20:]regr = linear_model.LinearRegression()regr_model = regr.fit(diabetes_X_train, diabetes_y_train)print(regr_model)print(regr_model.coef_)regr_precition = regr.predict(diabetes_X_test)# The mean square errorMSE = np.mean((regr_precition - diabetes_y_test) ** 2)print(MSE)# Explained variance score: 1 is perfect predictionand 0 means that there # is no linear relationship between X and y.Variance_score = regr.score(diabetes_X_test, diabetes_y_test)print(Variance_score)X = np.c_[0.5, 1.0].Ty = [0.5, 2]test_X = np.c_[0.5, 2]print(X)#============================================================# Model selection: choosing estimators and their parameters#============================================================digits = datasets.load_digits()X_digits = digits.datay_digits = digits.targetsvc = svm.SVC(C = 1, kernel = 'linear')var_score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])print(var_score)#============================================================#            Score, and cross-validated scores#============================================================X_folds = np.array_split(X_digits, 3)y_folds = np.array_split(y_digits, 3)X_train = list(X_folds)X_test = X_train.pop(0)X_train = np.concatenate(X_train)y_train = list(y_folds)y_test = y_train.pop(0)y_train = np.concatenate(y_train)scores = list()for k in range(3):	# We use 'list' to copy, in order to 'pop' later on 	X_train = list(X_folds)	X_test = X_train.pop(k)	X_train = np.concatenate(X_train)	y_train = list(y_folds)	y_test = y_train.pop(k)	y_train = np.concatenate(y_train)	scores.append(svc.fit(X_train, y_train).score(X_test, y_test))print(scores)from sklearn.model_selection import KFold, cross_val_scorefrom sklearn.model_selection import KFold, cross_val_scoreX = ["a", "a", "b", "c", "c", "c"]k_fold = KFold(n_split = 3)print(k_fold)# for train_indices, test_indices in k_fold