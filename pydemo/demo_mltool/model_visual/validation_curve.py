# -*- coding: utf-8 -*-

"""
@author:
@date:
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve



def train_valid_scores(model, X, y, param_name, param_range, cv_method, scoring, n_jobs):
    train_scores, valid_scores = validation_curve(estimator = model,
                                                  X = X,
                                                  y = y,
                                                  param_name = param_name,
                                                  param_range = param_range,
                                                  cv = cv_method,
                                                  scoring = scoring,
                                                  n_jobs = n_jobs)
    train_scores_mean = np.mean(train_scores, axis = 1)
    train_scores_std = np.std(train_scores, axis = 1)
    valid_scores_mean = np.mean(valid_scores, axis = 1)
    valid_scores_std = np.std(valid_scores, axis = 1)
    return train_scores, valid_scores, train_scores_mean, train_scores_std, valid_scores_mean, valid_scores_std


def validationCurve(model_name, param_name, param_range,
                    train_scores_mean, train_scores_std, valid_scores_mean, valid_scores_std):
    plt.title("Validation Curve with %s" % model_name)
    plt.xlabel("$%s$" % param_name)
    plt.ylabel("Score")
    plt.ylim(0.0, 1.1)
    lw = 2
    plt.semilogx(param_range, train_scores_mean, label = "Training score", color = "darkorange", lw = lw)
    plt.fill_between(param_range,
                     train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std,
                     alpha = 0.2,
                     color = "darkorange",
                     lw = lw)
    plt.semilogx(param_range, valid_scores_mean, label = "Cross-validation score", color = "navy", lw = lw)
    plt.fill_between(param_range,
                     valid_scores_mean - valid_scores_std,
                     valid_scores_mean + valid_scores_std,
                     alpha = 0.2,
                     color = "navy",
                     lw = lw)
    plt.legend(loc = "best")
    plt.show()
