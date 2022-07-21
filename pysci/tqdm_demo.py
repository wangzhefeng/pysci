# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# **********************************************


# python libraries
import os
import sys
from tqdm import tqdm, trange #, tqdm_notebook, tnrange
import time








# 测试代码 main 函数
def main():
    for i in tqdm(range(10), desc = "1st loop"):
        for j in trange(100, desc = "2nd loop", leave = False):
            time.sleep(0.01)


if __name__ == "__main__":
    main()

