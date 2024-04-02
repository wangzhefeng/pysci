# -*- coding: utf-8 -*-

# ***************************************************
# * File        : shuffling_algorithm.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-02-17
# * Version     : 0.1.021701
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys

import numpy as np


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]










# 测试代码 main 函数
def main():
    L = [1, 2, 3, 4, 5]
    for i in reversed(range(len(L))):
        print(i, np.random.randint(0, i, 1)[0], np.random.randint(0, i + 1, 1)[0] % (i + 1))
        L[i] = L[np.random.randint(0, i, 1)[0] % (i + 1)]
    print(L)

if __name__ == "__main__":
    main()

