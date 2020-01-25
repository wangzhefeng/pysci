#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

#===========================================================
#                        codeing
#===========================================================

# sys
print(dir(sys))
print("-" * 100)
print(sys.__doc__)
print("-" * 100)
print(help(sys))
print("-" * 100)
print(sys.platform)
if sys.platform[:3] == "win":
	print("hello windows")
print("-" * 100)
print(sys.maxsize)
print("-" * 100)
print(sys.version)
print("-" * 100)
print(sys.path)
sys.path.append(r"E:\project")
print(sys.path)
print("-" * 100)
print(sys.modules)
print(list(sys.modules.keys()))
print(sys)
print(sys.modules["sys"])
print(sys.getrefcount(sys))
print(sys.builtin_module_names)
print("-" * 100)
try:
	raise IndexError
except:
	print(sys.exc_info())
print("-" * 100)

import traceback
def grail(x):
	raise TypeError("already got one")

try:
	grail("authur")
except:
	exc_info = sys.exc_info()
	print(exc_info[0])
	print(exc_info[1])
	print(exc_info[2])
	traceback.print_tb(exc_info[2])

