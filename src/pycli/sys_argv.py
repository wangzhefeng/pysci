# -*- coding: utf-8 -*-


# ***************************************************
# * File        : sys_argv.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-23
# * Version     : 0.1.072301
# * Description : 向 Python 脚本传递参数, 通过 sys 模块访问参数
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]






# 测试代码 main 函数
def main():
    print("You passed the following arguments:")
    print(sys.argv)


if __name__ == "__main__":
    main()

