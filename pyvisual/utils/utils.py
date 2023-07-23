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
from typing import List
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# 字体尺寸设置
# plt.rcParams["font.size"] = 10
title_fontsize = 12
label_fontsize = 8

# 设置 figure plt.tight_layout()
plt.rcParams["figure.autolayout"] = True

# 处理 matplotlib 字体问题
# print(mpl.matplotlib_fname())  # matplotlib font 目录
# print(mpl.get_cachedir())  # matplotlib font 缓存
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei"]
plt.rcParams["font.family"].append("SimHei")

warnings.filterwarnings("ignore")

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_heatmap(dfs, 
                 stat = "corr",  # 协方差矩阵: "cov"
                 method = "spearman", 
                 figsize = (5, 5), 
                 titles: List[str] = "", 
                 sort_col_list: List[str] = ["mqxh"],
                 show: bool = False, 
                 img_file_name: str = None):
    """
    相关系数、协方差矩阵热力图

    Args:
        dfs (_type_): _description_
        stat (str, optional): _description_. Defaults to "corr".
        figsize (tuple, optional): _description_. Defaults to (5, 5).
        title (str, optional): _description_. Defaults to "".
        show (bool, optional): _description_. Defaults to False.
        img_file_name (str, optional): _description_. Defaults to None.
    """
    fig, axs = plt.subplots(
        nrows = 1, ncols = len(dfs), 
        figsize = figsize, 
        # dpi = 540, 
        facecolor = "w"
    )
    for df_idx, df, title in zip(range(len(dfs)), dfs, titles):
        ax = axs[df_idx] if len(dfs) > 1 else axs
        # 计算相关系数矩阵或协方差矩阵
        if stat == "corr":
            stat_matrix = df.corr(method).sort_values(by = sort_col_list, ascending = False)
        elif stat == "cov":
            stat_matrix = df.cov().sort_values(by = sort_col_list, ascending = False)
        # 绘制相关系数矩阵热力图
        sns.heatmap(
            data = stat_matrix,
            annot = True, 
            annot_kws = {
                "size": 8
            },
            square = True, 
            # sns.diverging_palette(20, 220, n=256) or "YlGnBu" or "Blues"
            cmap = sns.diverging_palette(20, 220, n = 256),
            # linewidths = 0.1, 
            linecolor = 'w',
            center = 0,
            vmin = -1, 
            vmax = 1, 
            fmt = ".2f",
            cbar = False,
            ax = ax,
        )
        ax.xaxis.tick_top()
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
        # ax.set_xlabel("", fontsize = label_fontsize)
        # ax.set_ylabel("", fontsize = label_fontsize)
        ax.set_title(f"{title}相关系数矩阵热力图", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter(df, 
                 xcols, 
                 ycols, 
                 cate_cols, 
                 figsize = (5, 5), 
                 show: bool = False, 
                 img_file_name: str = None):
    """
    散点图
    scatter legend link ref: https://stackoverflow.com/questions/17411940/matplotlib-scatter-plot-legend
    """
    fig, axs = plt.subplots(nrows = 1, ncols = len(xcols), figsize = figsize)
    for idx, xcol, ycol, cate_col in zip(range(len(xcols)), xcols, ycols, cate_cols):
        # ax
        ax = axs[idx] if len(xcols) > 1 else axs
        # 散点图
        if cate_col is not None:
            sns.scatterplot(data = df, x = xcol, y = ycol, hue = cate_col, ax = ax)
        else:
            sns.scatterplot(data = df, x = xcol, y = ycol, ax = ax)
        
        ax.grid()
        ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_ylabel(ycol, fontsize = label_fontsize)
        ax.set_title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_reg(df, 
                     xcols, 
                     ycols, 
                     figsize = (5, 5),
                     show: bool = False, 
                     img_file_name: str = None):
    """
    带拟合曲线的散点图
    """
    col_len = len(xcols)
    fig, axs = plt.subplots(nrows = 1, ncols = col_len, figsize = figsize)
    for idx, xcol, ycol in zip(range(col_len), xcols, ycols):
        # ax
        ax = axs[idx] if len(xcols) > 1 else axs
        sns.regplot(
            data = df, 
            x = xcol, 
            y = ycol, 
            robust = True,
            ax = ax
        )
        
        ax.grid()
        ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_ylabel(ycol, fontsize = label_fontsize)
        ax.set_title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_lm(df, xcol, ycol, cate_col, show: bool = False):
    """
    带拟合曲线的散点图

    Args:
        df (_type_): _description_
        xcol (_type_): _description_
        ycol (_type_): _description_
        cate_col (_type_): _description_
        figsize (tuple, optional): _description_. Defaults to (8, 5).
        show (bool, optional): _description_. Defaults to False.
        img_file_name (str, optional): _description_. Defaults to None.
    """
    if cate_col is not None:
        sns.lmplot(
            data = df, 
            x = xcol, y = ycol, hue = cate_col, 
            robust = True,
            markers = ["o", "x"], 
            palette = "Set1"
        )
    else:
        sns.lmplot(
            data = df, 
            x = xcol, 
            y = ycol, 
            robust = True
        )
    # plt.xlabel(xcol, fontsize = label_fontsize)
    # plt.ylabel(ycol, fontsize = label_fontsize)
    plt.title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()


def plot_timeseries(df, ycols, cate_col, 
                    figsize = (7, 5), 
                    show: bool = False, 
                    img_file_name: str = None):
    """
    时间序列图

    Args:
        df (_type_): _description_
        ycols (_type_): _description_
        cate_col (_type_): _description_
        figsize (tuple, optional): _description_. Defaults to (7, 5).
        show (bool, optional): _description_. Defaults to False.
        img_file_name (str, optional): _description_. Defaults to None.
    """
    fig, axs = plt.subplots(nrows = 1, ncols = len(ycols), figsize = figsize)
    for idx, ycol in enumerate(ycols):
        # ax
        ax = axs[idx] if len(ycols) > 1 else axs
        # 线图
        sns.lineplot(
            data = df, x = df.index, y = ycol, hue = cate_col, 
            # style = "manner", 
            marker = "o", 
            ax = ax
        )
        
        ax.grid()
        # ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
        # ax.set_ylabel(ycol, fontsize = label_fontsize)
        ax.set_title(f"{ycol} 在不同 {cate_col} 下的对比图", fontsize = title_fontsize)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_matrix(df, 
                      cols: List, 
                      figsize = (10, 10), 
                      title: str = "", 
                      xlabel: str = None,
                      ylabel: str = None,
                      show: bool = False, 
                      img_file_name: str = None):
    """
    散点图矩阵

    Args:
        df (_type_): _description_
        cols (List): _description_
        figsize (tuple, optional): _description_. Defaults to (10, 10).
        title (str, optional): _description_. Defaults to "".
        show (bool, optional): _description_. Defaults to False.
        img_file_name (str, optional): _description_. Defaults to None.
    """
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = figsize)
    sns.pairplot(
        data = df[cols], 
        kind = "reg", 
        diag_kind = "kde", 
        corner = True
    )
    # ax.grid()
    # if xlabel is not None:
    #     ax.set_xlabel(xlabel, fontsize = label_fontsize)
    # if ylabel is not None:
    #     ax.set_ylabel(ylabel, fontsize = label_fontsize)
    # ax.set_title(f"{title} 的散点图矩阵", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)




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
