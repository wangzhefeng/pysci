#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
文档注释
'''

__author__ = "wangzhefeng"

print(__doc__)
print(__author__)


# =============================================================
# 岭回归(ridge regression)
# =============================================================
from sklearn import linear_model

# data
train_x = [[0, 0], [0, 0], [1, 1]]
train_y = [0, 0.1, 1]

# 普通模型
reg = linear_model.Ridge(alpha = 0.5) # alpha 是控制模型系数收缩量的复杂性参数
model = reg.fit(train_x, train_y)
print(model)
print(reg.coef_)
print(reg.intercept_)


# 广义交叉验证
alphas = [0.1, 1.0, 10.0]
reg = linear_model.RidgeCV(alphas = alphas)
model_cv = reg.fit(train_x, train_y)
print('=' * 32)
print(model_cv)
print(reg.coef_)
print(reg.intercept_)
print(reg.alpha_)