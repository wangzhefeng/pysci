# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.11.06
# * Version     : 1.0.0
# * Description : des
# * Link        : link
# **********************************************


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

