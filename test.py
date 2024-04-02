# -*- coding: utf-8 -*-

# ***************************************************
# * File        : test.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2024-02-16
# * Version     : 0.1.021621
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

import pandas as pd
import numpy as np

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class Father:
    
    def __init__(self, age: int):
        self.age = age
        print(f"age: {self.age}")

    def getAge(self):
        return self.age


class Son(Father):
    
    def __init__(self, age: int):
        """
        重写父类 Father 的属性
        """
        self.age = age


# 测试代码 main 函数
def main():
    # 子类的实例继承了父类的方法
    son = Son(18)
    print(son.getAge())

if __name__ == "__main__":
    main()
