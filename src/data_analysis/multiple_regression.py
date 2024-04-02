# -*- coding: utf-8 -*-

# ***************************************************
# * File        : multiple_regression.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-27
# * Version     : 0.1.072715
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def run_multiple_regression(data, xcols, ycol, regul: str = "lasso"):
    # data
    X = data[xcols].values
    y = data[ycol].values

    if regul == "ridge":
        # 标准化和模型
        reg = make_pipeline(
            StandardScaler(), 
            # MinMaxScaler(feature_range = (0, 1)), 
            Ridge(alpha = 0.5)
        )
        reg.fit(data[xcols], data[ycol])
        coefs = reg["ridge"].coef_
    elif regul == "lasso":
        # 标准化和模型
        reg = make_pipeline(
            StandardScaler(), 
            # MinMaxScaler(feature_range = (0, 1)), 
            Lasso(alpha = 0.1)
        )
        reg.fit(data[xcols], data[ycol])
        coefs = reg["lasso"].coef_
    else:
        # 标准化和模型
        reg = make_pipeline(
            StandardScaler(), 
            # MinMaxScaler(feature_range = (0, 1)), 
            LinearRegression()
        )
        reg.fit(data[xcols], data[ycol])
        coefs = reg["linearregression"].coef_
    
    # model result
    result = {}
    for metric, coef in zip(xcols, coefs):
        result[metric] = coef
    result_table = pd.DataFrame(result, index = [0])
    
    return result_table





# 测试代码 main 函数
def main():
    seed = np.random.seed(42)
    df  = pd.DataFrame({
        "x1": np.random.randn(100),
        "x2": np.random.randn(100),
        "x3": np.random.randn(100),
        "y": np.random.randn(100),
    })
    X = df[["x1", "x2", "x3"]].values
    y = df["y"].values
    
    # model = LinearRegression()
    # model.fit(X,y)
    # print(model.coef_)
    
    result_table = run_multiple_regression(df = df, xcols = ["x1", "x2", "x3"], ycol = "y")
    print(result_table.T)
    
if __name__ == "__main__":
    main()
