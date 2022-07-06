#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: tinker
@date: 2019-01-06
"""
class Solution:

	def twoSum(self, nums, target):
		"""
		:type nums: list[int]
		:type target: int
		:return type: list[int]
		:param nums:
		:param target:
		:return:
		"""
		dic = {}
		for i, num in enumerate(nums):
			if num in dic:
				return [dic[num], i]
			else:
				dic[target - num] = i

