#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 21:18:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution:
	def reverse1(self, x):
		"""
		# method 1
		:type x: int
		:type: int
		"""
		intMax = 2 ** 31 - 1
		intMin = -2 ** 31
		rev = 0
		sign = 1

		if x > intMax or x < intMin:
			return 0

		if x < 0:
			sign = -1
			x *= sign

		while x != 0:
			pop = x % 10
			x = int(x / 10)
			rev = rev * 10 + pop

		return 0 if rev > intMax or rev < intMin else rev * sign

	def reverse2(self, x):
		"""
		# method 2
		:type x: int
		:type: int
		"""
		sign = lambda x: x and (1, -1)[x < 0]
		# sign = (x > 0) - (x < 0)
		r = int(str(sign(x) * x)[::-1])
		# r = int(str(sign * x)[::-1])

		return (sign(x) * r, 0)[r > 2**31 - 1 and r < -2**31]





def main():
	x = -2147483649

	solution = Solution()
	res1 = solution.reverse1(x)
	print(res1)

	res2 = solution.reverse1(x)
	print(res2)

if __name__ == "__main__":
	main()
