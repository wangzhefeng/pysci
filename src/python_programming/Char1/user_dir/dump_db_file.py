#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"



from make_db_file import loadDbase

db = loadDbase()
for key in db:
	print(key, '=>\n ', db[key])

print(db['sue']['name'])