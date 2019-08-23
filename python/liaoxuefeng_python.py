#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#############################################################################
#                                      数字                                 #
#############################################################################
a = 100
if a >= 0:
	print(a)
else:
	print(-a)
# 整数和浮点数在计算机内部存储的方式是不同的;
# 整数运算永远是精确的(除法也是精确的); 而浮点数运算则可能会有四舍五入的误差;
print(3 / 100)
print('I\'m OK.')
print(r"I\'m OK.")
print(r"I'm OK.")
print('''line1
line2
line3''')
print(2 > 0 and 3 > 0)
print(2 > 0 or 3 < 0)
print(not True)
print(not False)
'''
import math
print(PI)
'''
################## 真除法 / Floot地板除法 #############
# '/' 除法的结果永远是浮点数 (精确地除法)
print(10 / 3) 
print(9 / 3)
# '//' 除法的结果永远是整数 (只取整数部分)
print(10 // 3)
# '%' 求余得到的永远是整数
print(10 % 3)




#################################################################################
#                               字符串                                          #
#################################################################################
#######################             字符编码            #########################
# 文件/浏览器                 内存/服务器
#   utf-8                       unicode
# str -->             num          --> bytes
# str -->    ascii/unicode/utf-8   --> bytes
# 编码发展：字符(str) --> 
# ascii(英文字母、数字、符号) --> 
# unicode(所有字符str) --> 
# utf-8(所有字符str)
#                                  
#                             (存储: bytes)                 (存储: bytes)              (存储: bytes) 
# str字符(打印、显示)表示：
# str：                         1 str = 1str 英文字母、符号、中文...
# str数字表示：
# ascii：                       1 str = 英文/符号/数字: 1 bytes = 8 bits
# unicode(内存/服务器)：        1 str = 英文/符号/数字：2 bytes
#                                     = 中文：          2 bytes
#                                     = 很生僻的字符：  4 bytes 
# utf-8(文件/浏览器)：          1 str = 英文/符号/数字：1 byte
#                                     = 中文：          3 bytes
#                                     = 很生僻字符:     4-6 bytes
# str字节表示
# bytes : b''
# 转义字符表示
# rotation: r''
######################################## b'str'##################################
# str显示(unicode)
x = 'ABC'
print(x)
# byte显示(unicode)
y = b'ABC'
print(y)
######################################## r'str' #################################
n1 = 123
print(n1)
n2 = 456.789
print(n2)
s1 = 'Hello, world'
print(s1)
s2 = 'Hello, \'Adam\''
print(s2)
s3 = r'Hello, "Bart"'
print(s3)
s4 = r'''Hello,
Lisa!'''
print(s4)
######################################## ord(str) / chr(numbner) #################
# 单个字符编码
# str <--> unicode(数字)
print(ord("中"))
print(chr(20013))
############################### encode() #########################################
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# str(unicode) --> bytes(ascii/utf-8)
## str(unicode) --> bytes(ascii) 
## result: b'ABC'
print('ABC'.encode('ascii'))
## str(unicode) --> bytes(ascii)  
## result: error
# print('中文'.encode('ascii'))
## str(unicode) --> bytes(utf-8)  
## result: b'\xe4\xb8\xad\xe6\x96\x87'
print('中文'.encode('utf-8'))
############################### decode() ###########################################
# 要把bytes变为str，就需要用decode()方法
# bytes --> str(ascii/utf-8)
## byte --> str(ascii)
b'ABC'.decode('ascii')
## byte --> str(utf-8)
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
############################### len() ##############################################
## str:   字符数，
## bytes: 字节数
print(len('ABC'))
print(len('中文'))
############################## %(格式化) ###########################################
# %(0n)d: 整数
# %(.n)f: 浮点数
# %s:     字符串
# %x:     十六进制数
# %%:     %的转义
# 形式： 'str' %s (num, 'str',...)
s1 = 72
s2 = 85
r = ((85-72) / 72) * 100
print('%.1f%%' % r)


###################################################################################
#                                   列表                                          #
###################################################################################



###################################################################################
#                                  字典                                           #
###################################################################################


###################################################################################
#                                   集合                                          #
###################################################################################
# 集合(set)可以看成是没有 value 的字典
s1 = set([1, 2, 3])
print(s1)
s2 = set([1, 2, 2, 3, 3])
print(s2)

s2.add(4)
s2.remove(4)
s1 & s2      # 交集
s1 | s2      # 并集
###################################################################################
#                                   函数                                          #
###################################################################################


###################################################################################
#                                   列表生成式                                    #
###################################################################################
L1 = [x * x for x in range(10)]
L2 = [m, n for m in "ABC" for n in "XYZ"]
L3 = [x.lower() for x in L0 if isinstance(x, str)]
###################################################################################
#                                  生成器                                         #
###################################################################################
L = (x * x for x in range(10))
next(L)
for x in L:
	print(x)
# 菲波那切数列函数
def fib(Num):
	n, a, b = 0, 0, 1
	while n < Num:
		print(b)
		a, b = b, a + b
		n += 1
	return "Done"

print(fib(10))

# 菲波那切数列生成器函数
def fib(Num):
	n, a, b = 0, 0, 1
	while n < Num:
		yield b
		a, b = b, a + b
		n += 1
	return "Done"

for x in fib(10):
	print(x)


g = fib(10)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 杨辉三角生成器函数
# 1
# 1, 1
# 1, 2, 1
# 1, 3, 3, 1
# 1, 4, 6, 4, 1
# 1, 5, 10, 10, 5, 1

def triangles():
	L = [1]
	while True:
		yield L
		L = [1] + [L[s] + L[s + 1] for s in range(len(L) - 1)] + [1]
	return 'Done'

n = 0
for x in triangles():
	print(x)
	n += 1
	if n = 20:
		break


###################################################################################
#                                   迭代器                                        #
###################################################################################
from collections import Iterable
from collections import Iterator

# 可迭代对象, 可以作用于for循环--------------------------
# str
print(isinstance('abc', Iterable))
# list
print(isinstance([1, 2, 3], Iterable))
# tuple
print(isinstance((1, 2, 3), Iterable))
# dict
print(isinstance({}, Iterable))
# set
print(isinstance(set([1, 2, 3]), Iterable))
# generator/ generator function
print(isinstance((x for x in range(10)), Iterable))

def fib(Num):
	n, a, b = 0, 0, 1
	while n < Num:
		yield b
		a, b = b, a + b
		n += 1
	return "Done"
print(isinstance(fib(6), Iterable))

print("--------")

# 迭代器, 可有next()函数不断返回值--------------------------
# str
print(isinstance('abc', Iterator))
# list
print(isinstance([1, 2, 3], Iterator))
# tuple
print(isinstance((1, 2, 3), Iterator))
# dict
print(isinstance({}, Iterator))
# set
print(isinstance(set([1, 2, 3]), Iterator))
# generator/ generator function
print(isinstance((x for x in range(10)), Iterator))

def fib(Num):
	n, a, b = 0, 0, 1
	while n < Num:
		yield b
		a, b = b, a + b
		n += 1
	return "Done"
print(isinstance(fib(6), Iterator))

print("---------")

# 生成器(generator)都是Iterator对象,----------------------------
# 但str,list,tuple,dict,set虽然是Iterable,却不是Iterator
# 把str,list,tuple,dict,set变成Iterator可以使用iter()函数
# str
print(isinstance(iter('abc'), Iterator))
# list
print(isinstance(iter([1, 2, 3]), Iterator))
# tuple
print(isinstance(iter((1, 2, 3)), Iterator))
# dict
print(isinstance(iter({}), Iterator))
# set
print(isinstance(iter(set([1, 2, 3])), Iterator))
###################################################################################
#                                   高阶函数                                      #
###################################################################################
print(dir(builtins))

def add(x, y, f):
	return f(x) + f(y)

print(add(-5, -6, abs))
###################################################################################
#                             map(), reduce(), filter()                           #

# map()--------------------------------------------------------------------
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

L = []
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	L.append(f(x))
print(L)

L = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)

# reduce()--------------------------------------------------------------------
##                     fn()
def fn(x, y):
	return x * 10 + y
# 1 * 10 + 3 = 13
# 13 * 10 + 5 = 135
# 135 * 10 + 7 = 1357
# 1357 * 10 + 9 = 13579
print(reduce(fn, [1, 3, 5, 7, 9]))

##                     char2num()
def char2num(s):
	return {'0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5, '6': 6,'7': 7,'8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))


##                     str2int()
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5, '6': 6,'7': 7,'8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(str2int('13579'))

##                     lambda()
def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('13579'))

#                      normalize()
def normalize(name):
    return name[0].upper() + name[1:].lower()
print(list(map(normalize, ['adam', 'LISA', 'barT'])))


# filter()--------------------------------------------------------------------
def is_odd(x):
	return x % 2 == 0
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

##                      生成素数函数
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n
def _not_divisible(n):
	return lambda x: x % n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
#                    
def is_palindrome(n):
    return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print(list(output))

#                序列反转方法
# str
L = 'python'
L_reversed1 = L[::-1]                    # 切片 步长
L_reversed2 = ''.join(list(reversed(L)))
L_reversed3 = ''.join(tuple(reversed(L)))
L_reversed4 = ''.join(reversed(L))        # builtins.str.join() / ''.join() / "".join()方法
## list
L = [1, 2, 3, 4]
L_reversed1 = L[::-1]
L_reversed2 = list(reversed(L))
## tuple
L = (1, 2, 3, 4)
L_reversed1 = L[::-1]
L_reversed2 = tuple(reversed(L))

# sorted()------------------------------------------------------------------
L = [36, 5, -12, 9, -21]
print(sorted(L))
print(sorted(L, key = abs))
print(sorted(L, key = abs, reverse = True))


S = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(S))
print(sorted(S, key = str.lower))
print(sorted(S, key = str.upper))
print(sorted(S, key = str.lower, reverse = True))


###################################################################################
#                                   返回函数                                      #
# 函数作为返回值
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
print(calc_sum(1, 2, 3))

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
	
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
print(lazy_sum(1, 3, 5, 7, 9)())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# 闭包
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)
###################################################################################
#                                   匿名函数                                      #
list(map(lambda x: x * x, range(1, 10)))

f = lambda x: x * x
f
f(5)

def built(x, y):
	return lambda: x * x + y * y

###################################################################################
#                                   装饰器                                        #
def now():
	print('2017-07-16')

f = now()
f()
now.__name__
f.__name__
# 假设要增强now()函数的功能,比如,在函数调用前后自动打印日志,
# 但又不希望修改now()函数的定义,这种在代码运行期间动态增加功能的方式
# 称之为“装饰器”(Decorator)
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print('2017-07-16')

now()
###################################################################################
#                                   偏函数                                        #



#==============================================================================
#                               面向对象编程
#==============================================================================

#==============================================================================
#                            类和实例

# 创建Student类,绑定累的属性name,score,
#定义类的方法print_score(),get_grade()
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score > 80:
            return 'B'
        else:
            return 'C'
bart
Student
# 创建类 Student 的实例 bart, 并调用实例的属性，方法
bart = Student('Bart Simpson', 59)
bart.name
bart.score
bart.print_score()
bart.get_grade()
# 创建 Student 的实例 myself，并调用实例的属性和方法
myself = Student('Tinker Wang', 100)
myself.name
myself.score
myself.print_score()
myself.get_grade()

#==============================================================================
#                访问限制

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 80:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad Score')
        
myself = Student('Tinker Wang', 100)
# 取属性name, score
myself.get_name()
myself._Student__name  # 外部访问私有变量
myself.get_score()
myself._Student__score # 外部访问私有变量
# 调用方法print_score(),get_grade()
myself.print_score()
myself.get_grade()
# 更改属性score
myself.set_score(79)
myself.get_score()

# 错误的设置变量,myself.__name和myself._Student__name不是一个变量
myself.__name = 'Zhefeng Wang'
myself.__score = 99

myself.get_name()
myself._Student__name
myself.get_score()
myself._Student__score

myself.__name
myself.__score

# 传入错误的参数
myself.set_score(101)

#==============================================================================
# 总结：
# 1.__name__:特殊变量，特殊变量是可以直接访问的，不是provite变量,
# 2.__name:私有变量，内部可以访问, 外部不可以访问
# 3._name:外部可以访问的,但是,“虽然可以被访问,但是,请视为私有变量,不要随意访问”

#在一个实例里：
# __girl__ 表示“你可以上我，我不是贞女”
# __girl 表示“我是贞女，你不能上我”
# _girl 表示“你虽然可以上我，但你应该把我看做贞女”
# girl 表示“我是荡妇，谁都可以上我”
#但是python仍然可以用 _Student__girl 强上贞女(__girl)
#==============================================================================


#==============================================================================
#                          继承和多态


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

ani = Animal()
ani.run()

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

tortoise = Tortoise()
tortoise.run()



# 类型
l = list()
isinstance(l, list)
isinstance(animal, Animal)
isinstance(dog, Animal)
isinstance(dog, Dog)
isinstance(cat, Animal)
isinstance(cat, Cat)



def run_twice(animal):
    animal.run()
    animal.run()

run_twice(ani)
run_twice(dog)
run_twice(cat)
run_twice(tortoise)

#==============================================================================
#                     获取对象信息

# type()
type(123)
type('string')
type(None)
type(abs)
type(ani)
type(dog)
type(123) == type(456)
type(123) == int
type('abc') == type('123')
type('abc') == str
type('abc') == type(123)

import types
def fn():
    pass
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type(x for x in range(10)) == types.GeneratorType


# isinstance()
ani = Animal()
dog = Dog()
isinstance(ani, Animal)
isinstance(dog, Dog)
isinstance(dog, Animal)
isinstance(dog, Dog) and isinstance(dog, Animal)
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))


# dir()
dir('ABC')
len('ABC')
'ABC'.__len__()

class MyDog(object):
    def __len__(self):
        return 100

dog2 = MyDog()
len(dog2)

# hasattr(), setattr(), getattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
getattr(obj, 'y')
obj.y
getattr(obj, 'z')  # AttributeError
getattr(obj, 'z', 404)
hasattr(obj, 'z')

hasattr(obj, 'power')
getattr(obj, 'power')
fn = getattr(obj, 'power')
fn
fn()

#==============================================================================
#                  实力属性和类属性 

 class Student(object):
     def __init__(self, name):
         self.name = name
# 通过self给实例对象绑定属性 name
s = Student('Bob')
s.name
# 通过实例变量给实例对象绑定属性 score
s.score = 90
s.score

hasattr(s, 'name')
hasattr(s, 'score')

# 创建类Student,并创建类的属性 name
class Student(object):
     name = 'Student'
# 创建实例 s
s = Student()
# 打印name属性,因为实例并没有name属性,所以会继续查找class的name属性
print(s.name)
# 打印类的name属性
print(Student.name)
# 给实例绑定name属性
s.name = 'Michael'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)
# 但是类属性并未消失，用Student.name仍然可以访问
print(Student.name) 
# 如果删除实例的name属性
del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)

###########################################################################
#                       SQLite database connection
###########################################################################
# 导入SQLite驱动
import sqlite3
# 连接到SQLite数据库,数据库文件是test.db,如果文件不存在,会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建游标
cursor = conn.cursor()

# 执行一条SQL语句,创建user表
# cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# 执行一条SQL语句,插入一条记录
# cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michal\')')

# 通过rowcount获得插入的行数
# print(cursor.rowcount)

# 查询表user中的记录 
cursor.execute('SELECT * FROM user WHERE id = ? AND name = ?', ('1', 'Michal'))
values = cursor.fetchall()
print(values)

# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()

###########################################################################
#                       pymysql database connection
###########################################################################
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host = 'localhost',
					 		 user = 'root',
					 	     password = '071400',
					 		 db = 'python_pymysql',
					 		 charset = 'utf8mb4',
					 		 cursorclass = pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('wangzhefengr@163.com', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('wangzhefengr@163.com',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


###########################################################################
#                       使用SQLAlchemy
###########################################################################
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义Users对象
class Users(Base):
	# 表的名字
	__tablename__ = 'users'
	# 表的结构
	email = Column(String(20), primary_key = True)
	password = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:071400@localhost:3306/python_pymysql')
# 创建DBSession
DBSession = sessionmaker(bind = engine)


# # 往数据库python_pymysql中的表users中插入一条记录------------------------------

# 创建session对象
session = DBSession()
# 创建新User对象
new_user = Users(email = 'wangzhefeng@businessmatrix.com.cn', 
	  			 password = 'very-serect')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session:
session.close()

# 在数据库python_pymysql中的表users进行查询--------------------------------------
# 创建Session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(Users).filter(Users.email == 'wangzhefengr@163.com').one()
# 打印类型和对象的name属性
print('type:', type(user))
print('name:', user.email)
# 关闭Session
session.close()