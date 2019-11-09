#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import traceback as tb

#===========================================================
#                        codeing
#===========================================================
print(sys.exc_info())
print(sys.exc_info()[2])



try:
	a = 1 / 0
except ZeroDivisionError:
	print(sys.exc_info())
	print(sys.exc_info()[2])
	tb.print_exc(file = sys.stdout)
