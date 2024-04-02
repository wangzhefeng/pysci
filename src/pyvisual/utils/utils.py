# -*- coding: utf-8 -*-

# ***************************************************
# * File        : utils.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-06-28
# * Version     : 0.1.062810
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
from typing import List, Tuple
import warnings

import pandas as pd
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
import seaborn as sns

# 字体尺寸设置
# plt.rcParams["font.size"] = 10
title_fontsize = 13
label_fontsize = 7

# style sheet config
plt.style.use("classic")
plt.style.use("seaborn-whitegrid")
plt.style.use("ggplot")

mpl.rcParams["axes.unicode_minus"] = False # 解决图像中的 “-” 负号的乱码问题
plt.rcParams["figure.autolayout"] = True  # 设置 figure plt.tight_layout()
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei"]  # 处理 matplotlib 字体问题, 支持中文(macOS)
plt.rcParams["font.family"].append("SimHei")  # 处理 matplotlib 字体问题
plt.rcParams["axes.grid"] = True  # axis grid
plt.rc('mathtext', default = 'regular')  # 支持数学符号

warnings.filterwarnings("ignore")

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def lifecycle_of_a_plot():
    import numpy as np
    import matplotlib.pyplot as plt
    print(plt.style.available)
    plt.style.use("fivethirtyeight")
    plt.rcParams.update({
        "figure.autolayout": True,
    })

    # data
    data = {
        'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60
    }
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    # plot
    def currency(x, pos):
        """
        The two arguments are the value and tick position

        Args:
            x ([type]): [description]
            pos ([type]): [description]
        """
        if x >= 1e6:
            s = "${:1.1f}M".format(x * 1e-6)
        else:
            s = "${:1.0f}K".format(x * 1e-3)
        return s
    
    fig, ax = plt.subplots(figsize = (8, 4))

    # bar
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation = 45, horizontalalignment = "right")
    
    # vertical line
    ax.axvline(group_mean, ls = "--", color = "r")
    
    # group text
    for group in [3, 5, 8]:
        ax.text(145000, group, "New Company", fontsize = 10, verticalalignment = "center")
        
    # 标题设置
    ax.title.set(y = 1.05)
    # 设置X轴限制、X轴标签、Y轴标签、主标题
    ax.set(xlim = [-10000, 140000], xlabel = "Total Revenue", ylabel = "Company", title = "Company Revenue")
    # ax.set_xlim([-10000, 140000])
    # ax.set_ylim([])
    # ax.set_xlabel("Total Revenue")
    # ax.set_ylabel("Company")
    # ax.set_title("Company Revenue")
    # 设置X轴主刻度标签格式
    ax.xaxis.set_major_formatter(currency)
    # ax.yaxis.set_major_formatter()
    # ax.xaxis.set_minor_formatter()
    # ax.yaxis.set_minor_formatter()
    # 设置X轴主刻度标签
    ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
    # ax.set_yticks()
    # ax.set_xticklabels()
    # ax.set_yticklabels()
    # 微调fig
    fig.subplots_adjust(right = 0.1)
    
    print(fig.canvas.get_supported_filetypes())
    fig.savefig("sale.png", transparent = False, dpi = 80, bbox_inches = "tight")
    plt.show()




# 测试代码 main 函数
def main():
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    x = [1, 3, 4, 6, 7, 9]
    y = [0, 0, 5, 8, 8, 8]
    classes = ['A', 'B', 'C']
    values = [0, 0, 1, 2, 2, 2]
    colors = ListedColormap(['r','b','g'])
    scatter = plt.scatter(x, y, c = values, cmap = colors)
    plt.legend(handles = scatter.legend_elements()[0], labels = classes)
    plt.show()

if __name__ == "__main__":
    main()
