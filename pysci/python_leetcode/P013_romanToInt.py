#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 18:02:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
		res, p = 0, "I"
		for c in s[::-1]:
			res, p = res - d[c] if d[c] < d[p] else res + d[c], c
		return res



def main():
	solution = Solution()
	res = solution.romanToInt(s = "MCMXCIV")
	print(res)


if __name__ == "__main__":
	main()
