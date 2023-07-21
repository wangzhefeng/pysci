#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"

from os import getenv
import pymssql

server = getenv('PYMSSQL_TEST_SERVER')
user = getenv('PYMSSQL_TEST_USERNAME')
password = getenv('PYMSSQL_TEST_PASSWORD')


conn = pymssql.connect(host = server,
					   user = user,
					   password = password,
					   database = 'tempdb')
cursor = conn.cursor()


cursor.execute("""
	IF OBJECT_ID('persons', 'U') IS NOT NULL DROP TABLE persons
	CREATE TABLE persons
		id INT NOT NULL,
		name VARCHAR(100),
		salesrep VARCHAR(100),
		PRIMARY KEY(id)"""
)
cursor.executemany(
	"INSERT INTO persons VALUES (%d, %s, %s)",
	[(1, 'John Smith', 'John Doe'),
	 (2, 'Jane Doe', 'John Doe'),
	 (3, 'Mike T.', 'Sarah H.')]
)
conn.commit()

cursor.execute("SELECT * FROM persons WHERE salesrep = %s", 'John Doe')
row = cursor.fetchone()

while row:
	print("ID=%d, NAME=%s" % (row[0], row[1]))
	row = cursor.fetchone()
	print(row)

cursor.close()
conn.close()





###########################################################################
# pymssql module reference


#---------------------------------------
# Module-level symbols
pymssql.apilevel          # '2.0'-'pymssql' strives for compliance with DB-API 2.0.
pymssql.paramstyle        # 'pyformat'-'pymssql' uses extended python format codes.
pymssql.threadsafety      # 1-Module may be shared, but not connections.



#---------------------------------------
# Functions
# Constructor for creating a connection to the database. Return a Connection object.
pymssql.connect(server = '192.168.1.252', # database host
                user = 'tom.dong',        #
                password = 'oig123456',
                database = 'WZF',
                timeout = 0,
                login_timeout = 60,
                charset = 'UTF-8',
                as_dict = False,
                host = '',
                appname = None,
                port = '1433',
                conn_properties = '',
                autocommit = False,
                tds_version = '7.1')

pymssql.get_dbversion()       # TBD
pymssql.set_max_connections(25)
pymssql.get_max_connections()
pymssql.set_wait_callback()

#---------------------------------------
# Connection class
# class pymssql.Connection(user, password, host, database, timeout, login_timeout, charset, as_dict)
# Create an instance of this class by calling constructor pymssql.connect()
Connection.autocommit(True/False)
Connection.close()
Connection.cursor()
Connection.commit()
Connection.rollback()



#---------------------------------------
# Cursor class
# class pymssql.Cursor
# This class represents a Cursor (in terms of Python DB-API specs) that is used to make queries against the database and
# obtaining results. You create Cursor instance by calling cursor() method on an open Connection connection project.

# Cursor object properties
Cursor.rowcount()
Cursor.connection()
Cursor.lastrowid()
Cursor.rownumber()
# Cursor object methods
Cursor.close()
Cursor.execute()
Cursor.executemany()
Cursor.fetchone()
Cursor.fetchmany()
Cursor.fetchall()
Cursor.nextset()

Cursor.__iter__()
Cursor.next()

Cursor.setinputsizes()
Cursor.setoutputsize()



#---------------------------------------
# Exception
# pymssql.StandardError
# pymssql.Warning
# pymssql.Error
# pymssql.InterfaceError




# pymssql.Noe
# pymssql.ColumnsWithoutNamesError
