# -*- coding: utf-8 -*-


# ***************************************************
# * File        : utils.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-06
# * Version     : 0.1.070623
# * Description : description
# * Link        : link
# * Requirement : 日期、时间相关的工具函数
# ***************************************************


# python libraries
import calendar
import datetime


def getMonthDays(year: int, month: int) -> int:
    """
    计算某年某月的天数

    :param year: _description_
    :type year: int
    :param month: _description_
    :type month: int
    :return: _description_
    :rtype: _type_
    """
    monthRange = calendar.monthrange(year, month)
    return monthRange[1]


def isLeapYear(year: int) -> bool:
    """
    判断某年是否是闰年

    :param year: _description_
    :type year: int
    :return: _description_
    :rtype: _type_
    """
    # method 1
    # if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    #     return True
    # else:
    #     return False
    # method 2
    if calendar.isleap(year):
        return True
    else:
        return False


def createCalendar(year: int, month: int):
    """
    生成某年某月的日历

    :param year: _description_
    :type year: int
    :param month: _description_
    :type month: int
    """
    print(calendar.month(year, month))


def getYesterday():
    """
    获取昨天的日期

    :return: _description_
    :rtype: _type_
    """
    today = datetime.date.today()
    one_day = datetime.timedelta(days = 1)
    yesterday = today - one_day
    return yesterday


def dayOfYear(year: int, month: int, day: int) -> int:
    """
    判断某一天是改年的第几天

    :param year: _description_
    :type year: int
    :param month: _description_
    :type month: int
    :param day: _description_
    :type day: int
    :return: _description_
    :rtype: int
    """
    one_day_of_year = datetime.date(year = int(year), month = int(month), day = int(day))
    start_of_year = datetime.date(year = int(year), month = 1, day = 1)
    return (one_day_of_year - start_of_year).days + 1


# 控制模块被全部导入的内容
__all__ = [
    "getMonthDays", 
    "isLeapYear", 
    "createCalendar", 
    "getYesterday", 
    "dayOfYear",
]




# 测试代码 main 函数
def main():
    # 计算某年某月的天数
    monthRange = getMonthDays(2022, 7)
    print(monthRange)

    # 判断某年是否是闰年
    is_leap_year = isLeapYear(2022)
    print(is_leap_year)

    # 生成某年某月的日历
    createCalendar(2022, 7)

    # 获取昨天的日期
    yesterday = getYesterday()
    print(yesterday)
    print(type(yesterday))

    # 获取某一天为该年的第几天
    day_of_year = dayOfYear(2022, 7, 6)
    print(day_of_year)


if __name__ == "__main__":
    main()

