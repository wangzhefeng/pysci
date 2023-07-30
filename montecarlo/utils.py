# -*- coding: utf-8 -*-

# ***************************************************
# * File        : utils.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-23
# * Version     : 0.1.072323
# * Description : description
# * Link        : https://www.yanxishe.com/TextTranslation/2679?from=leiphone
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
from typing import List, Tuple
import matplotlib.pyplot as plt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_prob_result(prob_lists: List, 
                     y_values: List, 
                     figsize: Tuple = (10, 5), 
                     xlabels: List = "Iterations", 
                     ylabels: List = "Probability",
                     show: bool = False, 
                     img_file_name: str = None):
    """
    概率结果可视化

    Args:
        prob_list (_type_): _description_
        y_value (_type_): _description_
        xlabel (str, optional): _description_. Defaults to "Iterations".
        ylabel (str, optional): _description_. Defaults to "Probability".
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(prob_lists), figsize = figsize)
    for axes_idx, prob_list, y_value, xlabel, ylabel in zip(range(len(prob_lists)), prob_lists, y_values, xlabels, ylabels):
        ax = axes[axes_idx] if len(prob_lists) > 1 else axes
        ax.axhline(y = y_value, color = "red", linestyle = "-", )
        ax.plot(prob_list)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)





# 测试代码 main 函数
def main():
    plot_prob_result(
        prob_lists = [[0.1, 0.2, 0.1, 0.2, 0.1, 0.2], [0.1, 0.2, 0.1, 0.2, 0.1, 0.2]], 
        y_values = [0.15, 0.14]
    )

if __name__ == "__main__":
    main()
