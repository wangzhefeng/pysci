# -*- coding: utf-8 -*-

# ***************************************************
# * File        : scatter_plot.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-21
# * Version     : 0.1.072122
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


def scatter_plot1(df, xlabel, *ylabels, imgpath = None):
    fig, axs = plt.subplots(figsize = (10, 7), sharey = True, tight_layout = True)
    for ylabel in ylabels:
        plt.scatter(df[xlabel], df[ylabel], label = ylabel)
        plt.title("%s VS %s" % (xlabel, ylabel))
        plt.xlabel("%s" % xlabel)
        plt.ylabel("%s" % ylabel)
        plt.legend()
    
    if imgpath:
        plt.savefig(imgpath)
    plt.show()


def scatter_plot2(df, xlabel, *ylabels, imgpath = None):
    """
    matlab plot style
    """
    fig, axs = plt.subplots(figsize = (10, 7), sharey = True, tight_layout = True)
    for ylabel in ylabels:
        plt.scatter(df[xlabel], df[ylabel], marker = "o", label = ylabel)
        plt.title("%s VS %s" % (xlabel, ylabel))
        plt.xlabel("%s" % xlabel)
        # plt.ylabel("%s" % ylabel)
        plt.legend()
        if imgpath:
            plt.savefig(imgpath)
        plt.show()


# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
