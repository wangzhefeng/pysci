# -*- coding: utf-8 -*-


# ***************************************************
# * File        : file_util.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-06
# * Version     : 0.1.070622
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys
from typing import Any, Iterator
from mmap import mmap


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def get_lines_simple(filename: str) -> Any:
    """
    读取 jsonline 格式的文件的每一行

    :param filename: _description_
    :type filename: str
    :return: _description_
    :rtype: Any
    """
    with open(filename, "rb") as f:
        return f.readlines()


def get_lines_iterator(filename: str) -> Iterator:
    """
    读取 jsonline 格式的文件的每一行

    :param filename: _description_
    :type filename: str
    :yield: _description_
    :rtype: Iterator
    """
    with open(filename, "rb") as f:
        for i in f:
            yield i


def get_lines_mmap(filename: str) -> Any:
    """
    读取大文件 jsonline 格式的文件的每一行
    文件的大小比内存大的处理方式

    :param filename: _description_
    :type filename: str
    :return: _description_
    :rtype: Any
    :yield: _description_
    :rtype: Iterator[Any]
    """
    with open(filename, "r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp:i+1].decode()
                tmp = i + 1




# 测试代码 main 函数
def main():
    filename = "file.txt"

    # test get_lines_simple()
    for e in get_lines_simple(filename):
        pass

    # test get_lines_iterator()
    for e in get_lines_iterator(filename):
        pass

    # test get_lines_mmap()
    for e in get_lines_mmap(filename):
        pass

if __name__ == "__main__":
    main()

