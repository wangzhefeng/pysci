# -*- coding: utf-8 -*-

# ***************************************************
# * File        : Timer.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-05-29
# * Version     : 0.1.052916
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
import datetime as dt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class Timer:
    """
    运行时间计算
    """
    
    def __init__(self):
        self.start_dt = None

    def start(self):
        self.start_dt = dt.datetime.now()
        print(self.start_dt)

    def stop(self):
        end_dt = dt.datetime.now()
        print(end_dt)
        print(f"Time taken: {end_dt - self.start_dt}")




# 测试代码 main 函数
def main():
    import time
    timer = Timer()
    start = timer.start()
    time.sleep(10)
    stop = timer.stop()

if __name__ == "__main__":
    main()
