#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '1234567',
                             db = 'tinker',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
cur = connection.cursor()
try:
	# Create a new record
	sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
	cur.execute(sql, ('webmaster@python.org', 'very-secret'))
	#connection is not autocommit by default, so you must commit to save your chages
	connection.commit()

	# Read a string record
	sql = "SELECT `id`, `password` FROM `users` WHERE `email` = %s"
	cur.execute(sql, ('webmaster@python.org'))
	result = cur.fetchone()
	print(result)
finally:
	connection.close()
