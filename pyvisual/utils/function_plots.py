# -*- coding: utf-8 -*-

# ***************************************************
# * File        : function_plots.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-09-10
# * Version     : 0.1.091017
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

import numpy as np
import matplotlib.pyplot as plt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def math_function_plot(func, x, imgpath = None):
    """
    matlab plot style
    """
    fig, axs = plt.subplots(figsize = (10, 7), sharey = True, tight_layout = True)
    plt.plot(x, func(x), label = "x")
    
    plt.title("function of x")
    plt.xlabel("x")
    plt.ylabel("function(x)")
    plt.legend()
    if imgpath:
        plt.savefig(imgpath)
    plt.show();




# 测试代码 main 函数
def main():
    x = np.random.randn(100)
    func = np.sin
    math_function_plot(func = func, x = x)

if __name__ == "__main__":
    main()
