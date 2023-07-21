# -*- coding: utf-8 -*-

# ***************************************************
# * File        : tqdm_demo.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-21
# * Version     : 0.1.072121
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
import time

from tqdm import tqdm, trange, tqdm_notebook, tnrange

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]







# 测试代码 main 函数
def main():
    for i in tqdm(range(10), desc = "1st loop"):
        for j in trange(100, desc = "2nd loop", leave = False):
            time.sleep(0.01)

if __name__ == "__main__":
    main()
