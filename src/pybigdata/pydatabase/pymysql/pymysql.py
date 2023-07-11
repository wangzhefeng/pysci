# -*- coding: utf-8 -*-


# ***************************************************
# * File        : pymysql.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-26
# * Version     : 0.1.072621
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# import os
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host = 'localhost',
							 user = 'root',
							 password = '123456',
							 db = 'zfwang_db',
							 charset = 'utf-8mb4',
							 cursorclass = pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
		cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

	# connection is not autocommit by default. So you must commit to save
	# you changes.
	connection.commit()

	with connection.cursor() as cursor:
		# read a single record
		sql = "SELECT 'id', 'passport' FROM 'user' WHERE 'email'=%s"
		cursor.execute(sql, ('webmaster@python.org',))
		result = cursor.fetchone()
		print(result)
finally:
	connection.close()