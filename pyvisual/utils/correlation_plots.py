# -*- coding: utf-8 -*-

# ***************************************************
# * File        : correlation_plots.py
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
from typing import List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *
from plotnine.data import mtcars

# 字体尺寸设置
plt.rcParams["font.size"] = 13

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_heatmap(dfs: List, 
                 stat: str = "corr",  # 协方差矩阵: "cov"
                 method: str = "pearson", 
                 figsize: Tuple = (5, 5), 
                 titles: List[str] = "", 
                 show: bool = False, 
                 img_file_name: str = None):
    """
    相关系数、协方差矩阵热力图
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(dfs), figsize = figsize)
    stat_matrixs = []
    for idx, df, title in zip(range(len(dfs)), dfs, titles):
        # ax
        ax = axes[idx] if len(dfs) > 1 else axes
        # 计算相关系数矩阵或协方差矩阵
        if stat == "corr":
            stat_matrix = df.corr(method)#.sort_values(by = sort_col_list, ascending = False)
        elif stat == "cov":
            stat_matrix = df.cov()#.sort_values(by = sort_col_list, ascending = False)
        # 绘制相关系数矩阵热力图
        sns.heatmap(
            data = stat_matrix, annot = True, annot_kws = {"size": 8}, 
            square = True, cmap = sns.diverging_palette(20, 220, n = 256), 
            linecolor = 'w', center = 0, vmin = -1, vmax = 1, 
            fmt = ".2f", cbar = False, ax = ax,
        )
        ax.xaxis.tick_top()
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
        ax.set_title(f"{title}相关系数矩阵热力图", fontsize = 13)
        
        # 收集相关系数、协方差矩阵
        stat_matrixs.append(stat_matrix)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)
        
    return stat_matrixs


def plot_heatmap(data):
    # TODO
    base_plot = (
        ggplot(data, aes(x = "index", y = "var", fill = "value", size = "abs_value")) + 
            geom_point(shape = "o", colour = "black") + 
            scale_size_area(max_size = 11, guide = False) +
            scale_fill_cmap(name = "RdYlBu_r") +
            coord_equal() +
            theme(dpi = 100, figure_size = (4, 4))
    )
    print(base_plot)

    # TODO
    base_plot = (
        ggplot(data, aes(x = "index", y = "var", fill = "value", size = "abs_value")) + 
            geom_point(shape = "s", colour = "black") + 
            scale_size_area(max_size = 10, guide = False) +
            scale_fill_cmap(name = "RdYlBu_r") +
            coord_equal() +
            theme(dpi = 100, figure_size = (4, 4))
    )
    print(base_plot)

    # TODO
    base_plot = (
        ggplot(data, aes(x = "index", y = "var", fill = "value", label = "value")) + 
            geom_tile(colour = "black") +
            geom_text(size = 8, colour = "white") +
            scale_fill_cmap(name = "RdYlBu_r") +
            coord_equal() +
            theme(dpi = 100, figure_size = (4, 4))
    )
    print(base_plot)




# 测试代码 main 函数
def main():
    mat_corr_without_index = np.round(mtcars.corr(), 1)
    mat_corr_with_index = np.round(mtcars.corr(), 1).reset_index()
    mydata = pd.melt(mat_corr_with_index, id_vars = "index", var_name = "var", value_name = "value")
    mydata["abs_value"] = np.abs(mydata["value"])
    print(mydata)

if __name__ == "__main__":
    main()
