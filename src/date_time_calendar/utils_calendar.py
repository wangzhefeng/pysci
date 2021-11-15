# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : https://docs.python.org/3.7/library/calendar.html
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


def func():
    pass


class DemoClass:
    """
    类说明文档
    """
    _class_config_param = 100  # 类私有不变量
    
    def __init__(self, id_):
        self.id = id_
        self.param_a = None  # 类公开变量
        self._internal_param = None  # 类私有变量
    
    def ClassDemoFunc(self):
        """
        类普通方法
        """
        pass
    
    def _ClassPrivateFunc(self):
        """
        类私有方法
        """
        pass


class _PrivateDemoClass:
    """
    私有类
    """
    
    def __init__(self):
        pass




# 测试代码 main 函数
def main():
    pass


if __name__ == "__main__":
    main()

