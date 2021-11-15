# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : https://docs.python.org/3.7/library/datetime.html#module-datetime
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





from datetime import datetime, timedelta
from datetime import timezone
import re

# ==========================================================
# Main functions
# datetime.datetime()
# datetime.datetime.now()
# datetime.datetime().strftime("%Y-%m-%d %H:%M:%S")
# datetime.datetime().strptime("%a, %b %d %H:%M")
# datetime.datetime().timestamp()
# datetime.datetime.fromtimestamp()
# datetime.datetime.utcfromtimestamp()
# datetime.timestamp()
# datetime.fromtimestamp()
# datetime.utcfromtimestamp()
# ==========================================================


# ==============================
# 创建 datetime
# ==============================
# 获取当前日期和时间(当地时间)
now = datetime.now()

# 将 datetime 转换为特定的字符串
now_formated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))
print(now_formated)

# 获取指定日期和时间(当地时间)
dt = datetime(2017, 11, 4, 23, 38, 44)
print(dt)

# ==============================
# datetime vs timestamp
# ==============================
# datetime转换为timestamp(当地时间)
print(now.timestamp())
print(dt.timestamp())

# timestamp 转换为 datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))    # 当地时间（北京）
print(datetime.utcfromtimestamp(t)) # 格林威治标准时间

# =============================
# datetime vs str
# =============================
# str 转换为 datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转换为 str
print(now.strftime('%a, %b %d %H:%M'))

# =============================
# datetime加减
# =============================
now = datetime.now()
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 1, hours = 12))

# =============================
# 本地时间转换为UTC时间(UTC+0:00)
# =============================
tz_utc_8 = timezone(timedelta(hours = 8))
dt = now.replace(tzinfo = tz_utc_8)
print(dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt2)

# =============================
# Example
# =============================
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    num = int(re.match(r'^UTC([+-]\d{1,2}):([0-5]\d)', tz_str).group(1))
    tz = timezone(timedelta(hours = num))
    dt = dt.replace(tzinfo = tz)
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
print(t1)

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
print(t2)
