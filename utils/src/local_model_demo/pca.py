#!/usr/bin/env python
# -*- coding utf-8 -*-


import numpy as np
import pandas as pd 
# import matplotlib.pyplot as plt 
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.sparse import linalg


"""
class sklearn.decomposition.PCA(
    n_components = None,  
    copy = True, 
    whiten = False, 
    svd_solver = "auto", 
    tol = 0.0, 
    iterated_power = "auto", 
    random_state = None
)

# Attributes:
    components_
    explained_variance_
    explained_variance_ratio_
    singular_vlues_
    mean_
    n_componens_
    n_features_
    n_samples_
    noise_variance_
"""


X = np.array([
    [-1, -1], 
    [-2, -1],
    [-3, -2],
    [1, 1],
    [2, 1],
    [3, 2]
])
pca = PCA(n_components = 1)
pca.fit(X)
print("X: %s" % X)
print("pca.explained_variance_: %s" % pca.explained_variance_)
print("pca.explained_variance_ratio_: %s" % pca.explained_variance_ratio_)
print("pca.singular_values_: %s" % pca.singular_values_)
print("pca.n_components_: %s" % pca.n_components_)
print("pca.components_: %s" % pca.components_)

print("pca.mean_: %s" % pca.mean_)
print("pca.n_features_: %s" % pca.n_features_)
print("pca.n_samples_: %s" % pca.n_samples_)
print("pca.noise_variance_: %s" % pca.noise_variance_)
