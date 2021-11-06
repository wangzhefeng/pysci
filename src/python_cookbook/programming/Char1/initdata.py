
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"



# data
bob = {
	'name': 'Bob Smith',
	'age': 42,
	'pay': 30000,
	'job': 'dev'
}

sue = {
	'name': 'Sue Jones',
	'age': 45,
	'pay': 40000,
	'job': 'hdw'
}

tom = {
	'name': 'Tom',
	'age': 50,
	'pay': 0,
	'job': None
}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == "__main__":
	print(db)
	for key in db:
		print(key, '=>\n', db[key])