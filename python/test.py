#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"


import pandas as pd


data_2013 = pd.read_excel("E:/project/data/concat_test/2013.xlsx", sheet = "sheet1")
print(data_2013.head(6))