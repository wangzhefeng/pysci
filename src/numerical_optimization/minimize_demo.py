#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.optimize import minimize
import numpy as np


"""
目标函数： min[(2+x1)/(1+x2) -3 * x1 + 4 * x3]
约束条件： x1, x2, x3 的范围都在 [0.1, 0.9] 范围内
"""

def fun(args):
    """
    待优化函数：[(2+x1)/(1+x2) -3 * x1 + 4 * x3]
    """
    a, b, c, d = args
    v = lambda x: (a + x[0]) / (b + x[1]) - c * x[0] + d * x[2]

    return v


def con(args):
    """
    约束条件：
        x1 - x1_min >= 0
        x1_max - x1 >= 0
        x2 - x2_min >= 0
        x2_max - x2 >= 0
        x3 - x3_min >= 0
        x3_max - x3 >= 0
    """
    x1_min, x1_max, x2_min, x2_max, x3_min, x3_max = args
    cons = (
        {
            "type": "ineq", 
            "fun": lambda x: x[0] - x1_min 
        },
        {
            "type": "ineq",
            "fun": lambda x: -x[0] + x1_max
        },
        {
            "type": "ineq",
            "fun": lambda x: x[1] - x2_min
        },
        {
            "type": "ineq",
            "fun": lambda x: -x[1] + x2_max
        },
        {
            "type": "ineq",
            "fun": lambda x: x[2] - x3_min
        },
        {
            "type": "ineq",
            "fun": lambda x: -x[2] + x3_max
        }
    )
    return cons


def optimizer():
    """
    目标函数优化器
    """
    # 目标函数系数
    args_fun = (2, 1, 3, 4)
    # 约束条件参数范围
    args_con = (
        0.1, 0.9,
        0.1, 0.9,
        0.1, 0.9
    )
    # 构造约束条件
    cons = con(args_con)
    # 设置优化变量初始猜测值
    x0 = np.asarray((0.5, 0.5, 0.5))
    # 目标函数优化
    res = minimize(fun(args_fun), 
                   x0, 
                   method = "SLSQP", 
                   constraints = cons)
    return res




def main():
    result = optimizer()
    print("优化得到的目标函数最小值：", result.fun)
    print("优化状态：", result.success)
    print("优化路径：", result.x)

if __name__ == "__main__":
    main()