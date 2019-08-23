#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'



from datetime import datetime, timedelta, timezone
import re

# Main functions
# datetime.now()
# datetime.timestamp()
# datetime.fromtimestamp()
# datetime.utcfromtimestamp()

# 获取当前日期和时间(当地时间)
now = datetime.now()
now_formated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(type(now))
print(now_formated)

# 获取指定日期和时间(当地时间)
dt = datetime(2017, 11, 4, 23, 38, 44)
print(dt)

# datetime转换为timestamp(当地时间)
print(now.timestamp())
print(dt.timestamp())

timestamp_start = datetime(1970, 1, 1, 8, 0, 0)
print(timestamp_start.timestamp())

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))    # 当地时间（北京）
print(datetime.utcfromtimestamp(t)) # 格林威治标准时间

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# datetime加减
now = datetime.now()
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 1, hours = 12))

# 本地时间转换为UTC时间(UTC+0:00)
now = datetime.now()
print(now)

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


# Example
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
