#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
分割字符串或文本文件并交互地进行分页
"""

def more(text, numlines = 15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input("More?") not in ['y', 'Y']:
            break


if __name__ == "__main__":
    import sys
    more(open(sys.argv[1]).read(), 10)