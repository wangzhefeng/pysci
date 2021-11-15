#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 22:10:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

class Solution:
	"""
	def isPalindrome(self, x):
		return int(str(abs(x))[::-1]) == x
	"""

	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0:
			return False

		r = 1
		while x / r >= 10:
			r *= 10

		while x:
			left, x = divmod(x, r)
			x, right = divmod(x, 10)
			if left != right:
				return False
			r //= 100

		return True


def main():
	x = 1221
	y = 12521
	solution = Solution()
	res_x = solution.isPalindrome(x)
	print(res_x)
	res_y = solution.isPalindrome(y)
	print(res_y)

if __name__ == "__main__":
	main()