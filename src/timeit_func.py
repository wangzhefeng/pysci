# -*- coding: utf-8 -*-


# ***************************************************
# * File        : timeit_func.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-23
# * Version     : 0.1.072301
# * Description : 评估函数运行时间
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys
import time
import functools


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def timeit_func(func):
    """
    分析代码运行时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"function used: {end - start}")
    
    return wrapper


def timeit_script():
    pass





# 测试代码 main 函数
def main():
    @timeit_func
    def test_func(a):
        print(a)
        print("a")

    test_func("b")


if __name__ == "__main__":
    main()

