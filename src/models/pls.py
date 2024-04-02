#!/usr/bin/env python
# -*- coding utf-8 -*-



import numpy as np
import pandas as pd
import sklearn
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler



X = np.array([
    [0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0],
    [2.0, 2.0, 2.0],
    [2.0, 5.0, 4.0]
])
Y = np.array([
    [0.1, -0.2],
    [0.9, 1.1],
    [6.2, 5.9],
    [11.9, 12.3]
])
pls2 = PLSRegression(n_components = 2)
pls2.fit(X, Y)

Y_pred = pls2.predict(X)
print(Y_pred)
