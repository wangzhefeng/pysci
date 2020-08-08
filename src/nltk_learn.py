#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wangzhefeng'


import nltk
# nltk.download()
from nltk.book import *

# ====================
# texts()
# sents()

# print(text1)
# print(text2)
# print(text3)
# print(text4)
# print(text5)
# print(text6)
# print(text7)
# print(text8)
# print(text9)
#
# print(sent1)
# print(sent2)
# print(sent3)
# print(sent4)
# print(sent5)
# print(sent6)
# print(sent7)
# print(sent8)
# print(sent9)
# =================
text1.concordance("monstrous")
text2.concordance("affection")
text3.concordance("lived")
text1.similar("monstrous")
text2.common_contexts(["monstrous", "very"])
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text3.generate()
len(text3)
set(text3)
sorted(set(text3))
len(set(text3))
len(text3) / len(set(text3))

# 计算一个单词在文本中出现的次数及占比
text3.count("smote")
100 * text4.count("a") / len(text4)

def lexical_diversity(text):
	return len(text) / len(set(text))

def percentage(count, total):
	return 100 * count/ total
# ===============================================================
sent1 = ['Call', 'me', 'Ishmael', '.']
print(sent1)
len(sent1)
lexical_diversity(sent1)
print(sent1 + sent2)
sent1.append("Some")
print(text4[173])
text4.index("awaken")

