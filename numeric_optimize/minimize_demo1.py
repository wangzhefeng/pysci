#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.optimize import minimize
import numpy as np

"""
计算 1/x + x 的最小值
"""

def fun(args):
    a = args
    v = lambda x: a / x[0] + x[0]

    return v


def main():
    args = (1)
    # 初始值
    x0 = np.asarray((2))
    res = minimize(fun(args), x0, method = "SLSQP")
    print(res.fun)
    print(res.success)
    print(res.x)


if __name__ == "__main__":
    main()
