#!/usr/bin/env python
# -*- coding: utf-8 -*-



print('-------------------------------------------------------------------------')
def fetcher(obj, index):
	return obj[index]

x = 'spam'
print(fetcher(x, 3))


# ---------------------------------------------
# 默认异常处理器
# print(fetcher(x, 4))


# ---------------------------------------------
# 捕获异常
try:
	fetcher(x, 4)
except IndexError:
	print("Got exception!")


def catcher():
	try:
		fetcher(x, 4)
	except IndexError:
		print("Got Exception!")
	print('continuing')

catcher()
print('----------------------------')


# ---------------------------------------------
# 引发异常
try:
	raise IndexError
except IndexError:
	print("Got Exception")

# raise IndexError
# assert False, 'Nobody excepts the Spanish Inquisition'

# ---------------------------------------------
# 用户定义的异常
class Bad(Exception):
	pass

def doomed():
	raise Bad()

try:
	doomed()
except Bad:
	print("Got Bad")

# ---------------------------------------------
# 终止行为
try:
	fetcher(x, 3)
finally:
	print("Got Bad!")

def after():
	try:
		fetcher(x, 3)
	finally:
		print("after fetch")
	print('after try?')

after()

# ================================================


# try/except/else
# def action():
# 	return 1 + 1
#
# try:
# 	action()
# except:
# 	print('something')
# except NameError:
# 	print('statements')
# except IndexError as data:
# 	print('statements')
# except KeyError, value2:
# 	print('statements')
# except (AttributeError, TypeError):
# 	print('statements')
# except (AttributeError, TypeError, SyntaxError), value3:
# 	print('statements')
# else:
# 	print('statements')
# finally:
# 	print('statements')

# try/else

# try/finally
class MyError(Exception):
	pass

def stuff(file):
	raise MyError()

file = open('data', 'w')

try:
	stuff(file)
finally:
	file.close()
print('Not reached!')


# -----------------------------------------
sep = "_" *32 + '\n'
print(sep + "EXCEPTION RAISE AND CAUGHT")
try:
	x = 'spam'[99]
except IndexError:
	print('except run')
finally:
	print('finally run')
print('after run')


print(sep + "NO EXCEPTION RAISED")
try:
	x = 'spam'[3]
except IndexError:
	print('except run')
finally:
	print('finally run')
print('after run')

print(sep + "NO EXCEPTION RAISED, WITH ELSE")
try:
	x = 'spam'[3]
except IndexError:
	print('except run')
else:
	print('else run')
finally:
	print('finally run')
print('after run')


print(sep + "EXCEPTION RAISED AND CAUGHT")
try:
	x = 1 / 0
except ZeroDivisionError:
	print('except run')
finally:
	print('finally run')
print('after run')


print(sep + "EXCEPTION RAISED BUT NOT CAUGHT")
try:
	x = 1 / 0
except IndexError:
	print('except run')
finally:
	print('finally run')
print('after run')

# --------------------------------------------
# Raise

# raise instance
# raise class
# raise















print('-------------------------------------------------------------------------')