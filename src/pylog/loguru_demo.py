# -*- coding: utf-8 -*-

# ***************************************************
# * File        : loguru.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-05-31
# * Version     : 0.1.053109
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

from loguru import logger

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]




@logger.catch
def my_func(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)




# 测试代码 main 函数
def main():
    # 
    logger.debug("this is a debug message")
    # 
    logger.add("pysci/pylog/runtime.log")
    logger.debug("this is a debug message")
    #
    res = my_func(0, 0, 0)
    logger.info(f"my_func res={res}")
    
    

if __name__ == "__main__":
    main()
