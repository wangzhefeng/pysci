
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"


from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('sue', sue), ('tom', tom)]:
	recfile = open(key + '.pkl', 'wb')
	pickle.dump(record, recfile)
	recfile.close()


