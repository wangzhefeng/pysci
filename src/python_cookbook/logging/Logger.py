#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import ctypes



"""
设置log输出的字体颜色
"""
FOREGROUND_WHITE = 0x007
FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN = 0x02
FOREGROUND_RED = 0x04
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE = - 11
std_output_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle = std_output_handle):
	bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
	return bool

class Logger:
	def __init__(self, path, Clevel = logging.DEBUG, Flevel = logging.DEBUG):
		'''
		* 定义一各log类
		'''
		self.logger = logging.getLogger(path)
		self.logger.setLevel(logging.DEBUG)
		fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
		
		# 设置CMD日志
		sh = logging.StreamHandler()
		sh.setFormatter(fmt)
		sh.setLevel(Clevel)
		
		# 设置文件格式
		fh = logging.FileHandler(path)
		fh.setFormatter(fmt)
		fh.setLevel(Flevel)

		self.logger.addHandler(sh)
		self.logger.addHandler(fh)

	def debug(self, message, color = FOREGROUND_BLUE):
		set_color(color)
		self.logger.debug(message)
		set_color(FOREGROUND_WHITE)

	def info(self, message, color = FOREGROUND_GREEN):
		set_color(color)
		self.logger.info(message)
		set_color(FOREGROUND_WHITE)

	def warn(self, message, color = FOREGROUND_YELLOW):
		set_color(color)
		self.logger.warn(message)
		set_color(FOREGROUND_WHITE)

	def error(self, message, color = FOREGROUND_RED):
		set_color(color)
		self.logger.error(message)
		set_color(FOREGROUND_WHITE)

	def critical(self, message, color = FOREGROUND_RED):
		set_color(color)
		self.logger.critical(message)
		set_color(FOREGROUND_WHITE)


# if __name__ == "__main__":
# 	logyyx = Logger(path = "yyx.log", Clevel = logging.ERROR, Flevel = logging.DEBUG)
# 	logyyx.debug(message = "一个debug信息")
# 	logyyx.info(message = "一个info信息")
# 	logyyx.warn(message = "一个warning信息")
# 	logyyx.error(message = "一个error信息")
# 	logyyx.critical(message = "一个致命critical信息")





