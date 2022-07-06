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


def get_discount(level):
    if level == 1:
        "大量计算代码"
        discount = 0.1
    elif level == 2:
        "大量计算代码"
        discount = 0.2
    elif level == 3:
        discount = 0.3
    elif level == 4:
        discount = 0.4
    elif level == 5:
        discount = 0.5
    elif level == 6:
        discount = 3 + 2 - 5 * 0.1
    else:
        return "等级错误"
    return discount


def parse_level_1():
    "大量计算代码"
    discount = 0.1
    return discount


def parse_level_2():
    "大量计算代码"
    discount = 0.2
    return discount


def parse_level_2():
    "大量计算代码"
    discount = 0.2
    return discount


def parse_level_3():
    "大量计算代码"
    discount = 0.3
    return discount


def parse_level_4():
    "大量计算代码"
    discount = 0.4
    return discount


def parse_level_5():
    "大量计算代码"
    discount = 0.5
    return discount


def parse_level_6():
    "大量计算代码"
    discount = 3 + 2 - 5 * 0.1
    return discount

discount_map = {
    1: parse_level_1(),
    2: parse_level_2(),
    3: parse_level_3(),
    4: parse_level_4(),
    5: parse_level_5(),
    6: parse_level_6(),
}









# 测试代码 main 函数
def main():
    # method 1
    level = 1
    discount = get_discount(level)
    print(discount)

    # method 2
    level = 1
    discount = discount_map.get(level, "等级错误")
    print(discount)

if __name__ == "__main__":
    main()

