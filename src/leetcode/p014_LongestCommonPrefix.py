#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-02 16:48:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

class Solution():
	
	def LongestPrefix(self, strs):
		"""
        :type strs: List[str]
        :rtype: str
        """
		i = 0
		for x in zip(*strs):
			if len(set(x)) > 1:
				return strs[0][:i]
			i += 1
		return strs[0][:i] if strs else ""
