#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sklearn import svm

# data
train_x = [[0, 0], [1, 1]]
test_x = [[2, 2]]
train_y = [0, 1]

# model
clf = svm.SVC()
model = clf.fit(train_x, train_y)
print(model)

# 获得支持向量
print(clf.support_vectors_)
# 获得支持向量的索引get indices of support vectors
print(clf.support_)
# 为每一个类别获得支持向量的数量
print(clf.n_support_)


prediction = clf.predict(test_x)
print(prediction)


# train_x = digits.data[:-1]
# train_y = digits.target[:-1]
# test_x = digits.data[-1:]
#
# clf = svm.SVC(gamma = 0.001, C = 100.0)
# fit = clf.fit(train_x, train_y)
# print(fit)
#
# predict = clf.predict(test_x)
# print(predict)