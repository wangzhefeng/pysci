# -*- coding: utf-8 -*-


# ***************************************************
# * File        : demo.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-22
# * Version     : 0.1.072200
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys

import numpy as np
import pandas as pd

import dask.dataframe as dd
import dask.array as da
import dask.bag as db


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]
GLOBAL_VARIABLE = None


# dask object
index = pd.date_range("2021-09-01", periods = 2400, freq = "1H")
df = pd.DataFrame({
    "a": np.arange(2400),
    "b": list("abcaddbe" * 300),
}, index = index)
ddf = dd.from_pandas(df, npartitions = 10)
print(ddf, "\n")
print(ddf.divisions, "\n")
print(ddf.partitions[0], "\n")


# dask index
print(ddf.b, "\n")
print(ddf["2021-10-01":"2021-10-09 05:00:00"], "\n")


# computation
print(ddf["2021-10-01":"2021-10-09 05:00:00"].compute(), "\n")





























# 测试代码 main 函数
def main():
    pass


if __name__ == "__main__":
    main()

