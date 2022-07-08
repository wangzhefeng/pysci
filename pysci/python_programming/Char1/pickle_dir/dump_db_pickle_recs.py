
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"


import pickle
import glob

for filename in glob.glob('*.pkl'):
	recfile = open(filename, 'rb')
	record = pickle.load(recfile)
	print(filename, '=>\n', record)

suefile = open("sue.pkl", 'rb')
print(pickle.load(suefile)['name'])