#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#===========================================================
#                        codeing
#===========================================================

# 字符串方法
mystr = "\t WangZhefeng \n"
print(mystr.lower())
print(mystr.upper())
print(mystr.isalpha())
print(mystr.isdigit())
print(mystr.find("Zhe"))
print(mystr.replace("Zhe", "zhe"))
print(mystr.strip())
print(mystr.rstrip())
print(mystr.lstrip())
mystr2 = "aaa,bbb,ccc"
print(mystr2.split(","))
mystr3 = "a b\nc\nd"
print(mystr3.split())
print(mystr3.splitlines())
print("Ni".join(["aaa", "bbb", "ccc"]))
print(' '.join(["A", "dead", "parrot"]))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.whitespace)
mystr = "xxaaxxaa"
print("SPAM".join(mystr.split("aa")))
print(int("42"))
print(eval("42"))
print(str(42))
print(repr(42))
print(("%d" % 42))
print("{:d}".format(42))
print("42" + str(1))
print(int("42") + 1)