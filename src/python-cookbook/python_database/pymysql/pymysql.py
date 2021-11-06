#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 21:55:51
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

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