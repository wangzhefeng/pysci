# -*- coding: utf-8 -*-

# ***************************************************
# * File        : utils.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-23
# * Version     : 0.1.072323
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

import matplotlib.pyplot as plt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_prob_result(prob_list, y_value, xlabel = "Iterations", ylabel = "Probability"):
    # 概率结果可视化
    fig = plt.figure()
    plt.axhline(y = y_value, color = "red", linestyle = "-", )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(prob_list)
    plt.show()




# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
