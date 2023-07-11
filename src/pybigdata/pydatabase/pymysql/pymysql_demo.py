# -*- coding: utf-8 -*-


# ***************************************************
# * File        : pymysql_example.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-26
# * Version     : 0.1.072621
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234567',
    db = 'tinker',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor,
)
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
