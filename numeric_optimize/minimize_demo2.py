#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
from scipy.optimize import minimize
import numpy as np

"""
scipy.optimize.minimize(fun, 
                        x0, 
                        args = (), 
                        method = 'SLSQP', 
                        jac = None, 
                        bounds = None, 
                        constraints = (), 
                        tol = None, 
                        callback = None, 
                        options = {
                            'func': None, 
                            'maxiter': 100, 
                            'ftol': 1e-06, 
                            'iprint': 1, 
                            'disp': False, 
                            'eps': 1.4901161193847656e-08
                        })
"""

def fun(args):
    """
    待优化函数：[1 / x + x]
    """
    a = args
    v = lambda x: a / x[0] + x[0]

    return v


def con(args):
    """
    约束条件：
        None
    """
    pass


def optimizer():
    args_fun = (1)
    args_con = None
    x0 = np.asarray((2))
    res = minimize(fun = fun(args_fun), x0 = x0, method = "SLSQP")

    return res


def main():
    result = optimizer()
    print("优化得到的目标函数最小值：", result.fun)
    print("优化状态：", result.success)
    print("优化路径：", result.x)

if __name__ == "__main__":
    main()
