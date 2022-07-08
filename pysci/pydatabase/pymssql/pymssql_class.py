
# -*- coding: utf-8 -*-

import pymssql
import re
import lxml.html
import requests

# database config
# server = 'localhost'
# user = 'SA'
# password = 'Alvin123'
# database = 'TestDB'


class SQLServer:
	# 初始化构造方法
	def __init__(self, host, user, pwd, db):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db

	# 获取SQL Server数据哭连接
	def __GetConnect(self):
		if not self.db:
			raise(NameError, '没有设置数据库连接信息')
		self.conn = pymssql.connect(host = self.host,
		                            user = self.user,
		                            password = self.pwd,
		                            database = self.db)
		cur = self.conn.cursor()
		if not cur:
			raise(NameError, '数据库连接失败')
		else:
			return cur
	
	# 执行SQL查询
	def ExecQuery(self, sql):
		cur = self.__GetConnect()
		cur.execute(sql)
		# 以tuple列表的形式返回结果集中的全部数据
		resList = cur.fetchall()
		# 关闭查询执行连接
		self.conn.close()
		return resList

	def ExecQueryMany(self, sql):
		cur = self.__GetConnect()
		cur.executemany(sql)
		resList = cur.fetchall()
		self.conn.close()
		return resList

	# 关闭数据库连接
	def ExecNonQuery(self, sql):
		cur = self.__GetConnect()
		cur.execute(sql)
		self.conn.commit()
		self.conn.close()






# create a table
sql_create_table = """
	IF OBJECT_ID('TEMPDB..#tinker') IS NOT NULL BEGIN DROP TABLE tinker
	CREATE TABLE #tinker (
		id INT IDENTITY (1, 1) NOT NULL
		,name VARCHAR(255)
		,age INT
		,PRIMARY KEY(id)
	)
	"""
cur.execute(sql_create_table)

# insert multirow data
sql_insert_multi_data = """
	INSERT INTO #tinker VALUES(%d, %s, %s) %
	[(1, 'John Smith', 24), 
	 (2, 'Jane Doe', 25), 
	 (3, 'Mike T', 26)]
"""
cur.executemany(sql_insert_multi_data)
conn.commit()


# 查询数据
sql_select = """
	SELECT * 
	FROM #tinker
	WHERE name = %s % 'John Doe'
"""
cur.execute(sql_select)


# 遍历数据(存放到元组)
row = cur.fetchone()
while row:
	print("ID=%d, Name=%s" % (row[0], row[1]))
	row = cur.fetchone()

for row in cursor:
	print('row = %r' % (row,))


# 遍历数据(存放到字典)
cur = conn.cursor(as_dict = True)
cur.execute('SELECT * FROM #tinker WHERE name = %s', 'John Doe')
for row in cur:
	print("ID=%d, Name=%s" % (row['id'], row['name']))
conn.close()

# with 来避免手动关闭cursors和connection连接
import pymssql

server = "187.32.43.13"    # 连接服务器地址
user = "root"　　　　　　　# 连接帐号
password = "1234"　　　　　　# 连接密码

with pymssql.connect(server, user, password, "你的连接默认数据库名称") as conn:
    with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
        cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))

# 调用存储过程：
with pymssql.connect(server, user, password, "tempdb") as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute("""
        CREATE PROCEDURE FindPerson
            @name VARCHAR(100)
        AS BEGIN
            SELECT * FROM persons WHERE name = @name
        END
        """)
        cursor.callproc('FindPerson', ('Jane Doe',))
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))


# 2.使用_mssql连接sql server数据库并实现操作（官方api  http://www.pymssql.org/en/stable/ref/_mssql.html）
import _mssql
# 创建连接
conn = _mssql.connect(server='SQL01', user='user', password='password', \
    database='mydatabase')
print(conn.timeout)
print(conn.login_timeout)

# 创建table
conn.execute_non_query('CREATE TABLE persons(id INT, name VARCHAR(100))')
# insert数据
conn.execute_non_query("INSERT INTO persons VALUES(1, 'John Doe')")
conn.execute_non_query("INSERT INTO persons VALUES(2, 'Jane Doe')")
# 查询操作
conn.execute_query('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in conn:
    print "ID=%d, Name=%s" % (row['id'], row['name'])
#查询数量count()
numemployees = conn.execute_scalar("SELECT COUNT(*) FROM employees")
# 查询一条数据
employeedata = conn.execute_row("SELECT * FROM employees WHERE id=%d", 13)
# 带参数查询的几个例子：
conn.execute_query('SELECT * FROM empl WHERE id=%d', 13)
conn.execute_query('SELECT * FROM empl WHERE name=%s', 'John Doe')
conn.execute_query('SELECT * FROM empl WHERE id IN (%s)', ((5, 6),))
conn.execute_query('SELECT * FROM empl WHERE name LIKE %s', 'J%')
conn.execute_query('SELECT * FROM empl WHERE name=%(name)s AND city=%(city)s', \
    { 'name': 'John Doe', 'city': 'Nowhere' } )
conn.execute_query('SELECT * FROM cust WHERE salesrep=%s AND id IN (%s)', \
    ('John Doe', (1, 2, 3)))
conn.execute_query('SELECT * FROM empl WHERE id IN (%s)', (tuple(xrange(4)),))
conn.execute_query('SELECT * FROM empl WHERE id IN (%s)', \
    (tuple([3, 5, 7, 11]),))
#关闭连接
conn.close()





def main():
	mscon = SQLServer(host = 'localhost',
	                  user = 'SA',
	                  pwd = 'Alvin123',
	                  db = 'TestDB')
	sql = '''SELECT * 
			 FROM TestDB.dbo.Tinker_test'''
	mscon.ExecNonQuery(sql)

if __name__ == 'main':
	main()