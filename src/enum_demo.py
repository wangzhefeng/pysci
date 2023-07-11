# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022.01.05
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# **********************************************


# python libraries
import os
import sys
from enum import Enum, unique


# global variable
GLOBAL_VARIABLE = None


def demo():
    Month = Enum(
        "Month", 
        ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    )
    for name, member in Month.__members__.items():
        print(name, "=>", member, ",", member.value)


@unique
class Weekday(Enum):
    """
    星期枚举类型类
    """
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def test_weekday_class():
    day1 = Weekday.Mon
    print(day1)
    print(Weekday.Tue)
    print(Weekday["Tue"])
    print(Weekday.Tue.value)
    print(day1 == Weekday.Mon)
    print(Weekday(1))
    print(day1 == Weekday(1))
    for name, member in Weekday.__members__.items():
        print(name, "=>", member, ",", member.value)
    # Weekday.Mon.value = 7 # Weekday 不可变


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender
        




# 测试代码 main 函数
def main():
    demo()
    test_weekday_class()
    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')



if __name__ == "__main__":
    main()

