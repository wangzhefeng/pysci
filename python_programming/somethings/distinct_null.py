#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# ============================================================
# Series, DataFrame
# ============================================================
# list 去重
M = [1, 4, 3, 6, 5, 4, 3, 2, 7, 8]
distinct_M = list(set(M))
print(distinct_M)


# ============================================================
# DataFrame去重
mydata = pd.DataFrame({
	"a": ["A", "B", "C", "D", "B", "C"],
	"b": [43, 32, 56, 67, 32, 56]
})
print(mydata)

distinct_mydata = mydata.drop_duplicates()
print(distinct_mydata)

# ============================================================
# 缺失值处理
# ============================================================
# 计算
val = np.array([5, np.nan, 8, 9, np.nan])
print(val)

print(np.nansum(val))
print(sum(val))
print(np.sum(val))

print(np.nanmean(val))
print(np.mean(val))

print(np.nanmin(val))
print(min(val))
print(np.min(val))

print(np.nanmax(val))
print(max(val))
print(np.max(val))

# ======================================================
myseries = pd.Series(["A", "B", np.nan, "C"])
mydata = pd.DataFrame({
	"A": ["A", "B", "C", "D", "E", "F", np.nan],
	"B": [43, np.nan, 56, 67, np.nan, 56, np.nan]
})
# 识别缺失值
print(myseries.isnull())
print(myseries.notnull())

print(mydata.isnull())
print(mydata.notnull())
# =====================================================
# 去除缺失值
print(myseries.dropna())
print(mydata.dropna())

print("=" * 32)
print(mydata.dropna(axis = 0)) # row
print(mydata.dropna(how = "all", axis = 0)) # row
print(mydata.dropna(how = "any", axis = 0)) # row

print(mydata.dropna(axis = 1)) # column
print(mydata.dropna(how = "all", axis = 1)) # column
print(mydata.dropna(how = "any", axis = 1)) # column

# =====================================================
# 缺失值填充
print(myseries.fillna(value = 0))
print(mydata.fillna(value = 0))



