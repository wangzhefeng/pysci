# -*- coding: utf-8 -*-

"""
@author:
@date:
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve


def learningCurve(model, X, y,
                  train_sizes = np.array([0.1, 0.33, 0.55, 0.78, 1. ]),
                  cv_method = "warn", n_jobs = None):
    train_sizes, train_scores, valid_scores = learning_curve(estimator = model,
                                                             X = X,
                                                             y = y,
                                                             train_sizes = train_sizes,
                                                             cv = cv_method,
                                                             n_jobs = n_jobs)
    train_scores_mean = np.mean(train_scores, axis = 1)
    train_scores_std = np.std(train_scores, axis = 1)
    valid_scores_mean = np.mean(valid_scores, axis = 1)
    valid_scores_std = np.std(valid_scores, axis = 1)

    return train_sizes, train_scores, valid_scores, \
           train_scores_mean, train_scores_std, valid_scores_mean, valid_scores_std


def plot_learning_curve(model_name,
                        title,
                        train_scores_mean,
                        train_scores_std,
                        valid_scores_mean,
                        valid_scores_std,
                        ylim = None,
                        train_sizes = np.linspace(.1, 1.0, 5)):
    """
    Generate a simple plot of the test and training learning curve.
    """
    plt.figure()
    plt.title(title + "(%s)" % model_name)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.grid()

    plt.fill_between(train_sizes,
                     train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std,
                     alpha = 0.1,
                     color = "r")
    plt.fill_between(train_sizes,
                     valid_scores_mean - valid_scores_std,
                     valid_scores_mean + valid_scores_std,
                     alpha = 0.1,
                     color = "g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color = "r", label = "Training score")
    plt.plot(train_sizes, valid_scores_mean, 'o-', color="g", label = "Cross-validation score")

    plt.legend(loc = "best")
    return plt


