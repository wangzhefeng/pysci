# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.11.14
# * Version     : 1.0.0
# * Description : 日期、时间相关的工具函数
# * Link        : link
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


def getMonthDays(year: int, month: int):
    """
    计算某年某月的天数

    Args:
        year (int): [description]
        month (int): [description]

    Returns:
        [type]: [description]
    """
    import calendar
    monthRange = calendar.monthrange(year, month)
    return monthRange[1]


def isLeapYear(year: int):
    """
    判断某年是否是闰年

    Args:
        year (int): [description]

    Returns:
        [type]: [description]
    """
    # method 1
    # if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    #     return True
    # else:
    #     return False
    # method 2
    import calendar
    if calendar.isleap(year):
        return True
    else:
        return False


def createCalendar(year, month):
    """
    生成某年某月的日历

    Args:
        year ([type]): [description]
        month ([type]): [description]
    """
    import calendar
    print(calendar.month(year, month))


def getYesterday():
    """
    获取昨天的日期

    Returns:
        [type]: [description]
    """
    import datetime
    today = datetime.date.today()
    one_day = datetime.timedelta(days = 1)
    yesterday = today - one_day
    return yesterday


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


# 控制模块被全部导入的内容
__all__ = ["getMonthDays", "isLeapYear", "createCalendar", "getYesterday"]


# 测试代码 main 函数
def main():
    # 计算某年某月的天数
    monthRange = getMonthDays(2021, 11)
    print(monthRange)

    # 判断某年是否是闰年
    is_leap_year = isLeapYear(2020)
    print(is_leap_year)

    # 生成某年某月的日历
    createCalendar(2021, 11)

    # 获取昨天的日期
    yesterday = getYesterday()
    print(yesterday)




if __name__ == "__main__":
    main()

