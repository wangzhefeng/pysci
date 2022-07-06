# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


def variables():
    age: int = 1
    
    age = 1  # type: int
    
    a: int
    child: bool
    if age < 18:
        child = True
    else:
        child = False
    

def build_in_types():
    from typing import List, Set, Dict, Tuple, Optional

    x: int = 1
    x: float = 1.0
    x: bool = True
    x: str = "test"
    x: bytes = b"test"
    
    



# 测试代码 main 函数
def main():
    build_in_types()
    

    



if __name__ == "__main__":
    main()

