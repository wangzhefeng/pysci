# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.11.06
# * Version     : 1.0.0
# * Description : 
# *               1.logger：提供日志接口，供应用代码使用
# *             	 - logger 最常用的操作有两类：配置和发送日志消息
# *                  - 可以通过 logging.getLogger(name) 获取 logger 对象，如果不指定 name 则返回 root 对象，多次使用相同的 name 调用 getLogger 方法返回同一个 logger 对象
# *               2.handler：将日志记录(log record)发送到合适的目的地(destination)，比如文件，socket 等
# *             	 - 一个 logger 对象可以通过 addHandler 方法添加到多个 handler，每个 handler 又可以定义不同日志级别，以实现日志分级过滤显示
# *               3.filter：提供一种优雅的方式决定一个日志记录是否发送到 handler
# *               4.formatter：指定日志记录输出的具体格式
# *             	 - formatter 的构造方法需要两个参数：消息的格式字符串和日期字符串，这两个参数都是可选的
# *               5.日志级别
# *                 - NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
# *               6.logging 用法解析
# *               6.1 初始化 
# *             	  logger = logging.getLogger("endlesscode")
# *             	  getLogger()方法后面最好加上所要日志记录的模块名字，后面的日志格式中的 %(name)s 对应的是这里的模块名字
# *               6.2 设置级别
# *             	  logger.setLevel(logging.DEBUG)
# *             	  logging 中有 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL 这几种级别，日志会记录设置级别以上的日志
# *               6.3 Handler
# *             	  常用的是 StreamHandler 和 FileHandler，windows 下可以简单理解为一个是 console 和文件日志，一个打印在 CMD 窗口上，一个记录在一个文件上
# *               6.4 formatter
# *             	 定义了最终 log 信息的顺序, 结构和内容，比如这样的格式 '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'
# *             	  %(name)s 				Logger 的名字
# *             	  %(levelname)s 		文本形式的日志级别
# *             	  %(message)s 			用户输出的消息
# *             	  %(asctime)s 			字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# *             	  %(levelno)s 			数字形式的日志级别
# *             	  %(pathname)s 			调用日志输出函数的模块的完整路径名，可能没有
# *             	  %(filename)s 			 调用日志输出函数的模块的文件名
# *             	  %(module)s 			调用日志输出函数的模块名
# *             	  %(funcName)s 			调用日志输出函数的函数名
# *             	  %(lineno)d 			调用日志输出函数的语句所在的代码行
# *             	  %(created)f 			当前时间，用 UNIX 标准的表示时间的浮 点数表示
# *             	  %(relativeCreated)d 	输出日志信息时的，自 Logger 创建以 来的毫秒数
# *             	  %(thread)d 			线程 ID。可能没有
# *             	  %(threadName)s 		线程名。可能没有
# *             	  %(process)d 			进程 ID。可能没有
# *               6.5 记录 
# *             	  使用 object.debug(message) 来记录日志
# * Link        : link
# **********************************************


# python libraries
import logging
import ctypes


# 设置log输出的字体颜色
FOREGROUND_WHITE = 0x007
FOREGROUND_BLUE = 0x01
FOREGROUND_GREEN = 0x02
FOREGROUND_RED = 0x04
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN


# def set_color(color):
#     std_output_handle = ctypes.windll.kernel32.GetStdHandle(- 11)
#     bool = ctypes.windll.kernel32.SetConsoleTextAttribute(std_output_handle, color)
#     return bool


class Logger:
    """
    定义一个 log 类
    """
    def __init__(self, path, Clevel = logging.DEBUG, Flevel = logging.DEBUG):
        """
        Args:
            path ([type]): [description]
            Clevel ([type], optional): [description]. Defaults to logging.DEBUG.
            Flevel ([type], optional): [description]. Defaults to logging.DEBUG.
        """
        # 设置日志路径
        self.logger = logging.getLogger(path)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志格式
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Clevel)
        self.logger.addHandler(sh)
        # 设置文件格式
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(fh)

    def debug(self, message, color = FOREGROUND_BLUE):
        # set_color(color)
        self.logger.debug(message)
        # set_color(FOREGROUND_WHITE)

    def info(self, message, color = FOREGROUND_GREEN):
        # set_color(color)
        self.logger.info(message)
        # set_color(FOREGROUND_WHITE)

    def warn(self, message, color = FOREGROUND_YELLOW):
        # set_color(color)
        self.logger.warn(message)
        # set_color(FOREGROUND_WHITE)

    def error(self, message, color = FOREGROUND_RED):
        # set_color(color)
        self.logger.error(message)
        # set_color(FOREGROUND_WHITE)

    def critical(self, message, color = FOREGROUND_RED):
        # set_color(color)
        self.logger.critical(message)
        # set_color(FOREGROUND_WHITE)




def main():
    logyyx = Logger(path = "yyx.log", Clevel = logging.ERROR, Flevel = logging.DEBUG)
    logyyx.debug(message = "一个debug信息")
    logyyx.info(message = "一个info信息")
    # logyyx.warn(message = "一个warning信息")
    # logyyx.error(message = "一个error信息")
    # logyyx.critical(message = "一个致命critical信息")



if __name__ == "__main__":
    main()

