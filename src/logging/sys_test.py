#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys


temp_stdout = sys.stdout
temp_stderr = sys.stderr
-- ************************************************
sys.stderr = open("F:/log.txt", "a")
sys.stdout = open("F:/log.txt", "a")

a = 10 
print(a)

b = 0 
print(b)

c = a / b

sys.stderr.close()
sys.stdout.close()
-- ************************************************
sys.stderr = temp_stderr
sys.stdout = temp_stdout