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
from typing import List, Tuple

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 字体尺寸设置
# plt.rcParams["font.size"] = 10
title_fontsize = 13
label_fontsize = 7

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


# TODO
def scatter_plot(df, xlabel, *ylabels, imgpath = None):
    """
    matlab plot style
    """
    fig, axes = plt.subplots(figsize = (10, 7), sharey = True, tight_layout = True)
    for ylabel in ylabels:
        plt.scatter(
            df[xlabel],
            df[ylabel],
            marker = "o",
            label = ylabel,
        )
        plt.title("%s VS %s" % (xlabel, ylabel))
        plt.xlabel("%s" % xlabel)
        plt.ylabel("%s" % ylabel)
        plt.legend()
        
        if imgpath:
            plt.savefig(imgpath)
        plt.show()


def plot_scatter(df: pd.DataFrame, 
                 xcols: List[str], 
                 ycols: List[str], 
                 cate_cols: List[str], 
                 figsize: Tuple = (5, 5), 
                 show: bool = False, 
                 img_file_name: str = None):
    """
    散点图
    scatter legend link ref:
    https://stackoverflow.com/questions/17411940/matplotlib-scatter-plot-legend
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(xcols), figsize = figsize)
    for idx, xcol, ycol, cate_col in zip(range(len(xcols)), xcols, ycols, cate_cols):
        # ax
        ax = axes[idx] if len(xcols) > 1 else axes
        
        # 散点图
        if cate_col is not None:
            sns.scatterplot(data = df, x = xcol, y = ycol, hue = cate_col, ax = ax)
        else:
            sns.scatterplot(data = df, x = xcol, y = ycol, ax = ax)
        ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_ylabel(ycol, fontsize = label_fontsize)
        ax.set_title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
        ax.legend(loc = "best")
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_reg(df: pd.DataFrame, 
                     xcols: List[str], 
                     ycols: List[str], 
                     figsize: Tuple = (5, 5),
                     show: bool = False, 
                     img_file_name: str = None):
    """
    带拟合曲线的散点图
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(xcols), figsize = figsize)
    for idx, xcol, ycol in zip(range(len(xcols)), xcols, ycols):
        # ax
        ax = axes[idx] if len(xcols) > 1 else axes
        # 带拟合曲线的散点图
        sns.regplot(
            data = df, 
            x = xcol, 
            y = ycol, 
            # robust = True,
            lowess = True, 
            line_kws={"color": "C2"},  
            # y_jitter=0.03,
            order = 0, 
            scatter_kws = {"s": 20},
            ax = ax,
        )
        # axes config
        ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_ylabel(ycol, fontsize = label_fontsize)
        ax.set_title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_lm(df: pd.DataFrame, 
                    xcol: str, 
                    ycol: str, 
                    cate_col: str, 
                    show: bool = False, 
                    img_file_name: str = None):
    """
    带拟合曲线的散点图
    """
    # fig = plt.figure(figsize = figsize)
    if cate_col is not None:
        sns.lmplot(
            data = df, x = xcol, y = ycol, hue = cate_col, 
            robust = True, 
            # lowess = True,
        )
    else:
        sns.lmplot(data = df, x = xcol, y = ycol, robust = True)
    plt.title(f"{xcol} 与 {ycol} 相关关系散点图", fontsize = title_fontsize)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    # if img_file_name is not None:
    #     fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)


def plot_scatter_matrix(df: pd.DataFrame, 
                        cols: List, 
                        figsize: Tuple = (10, 10), 
                        xlabel: str = None,
                        ylabel: str = None,
                        title: str = "", 
                        show: bool = False, 
                        img_file_name: str = None):
    """
    散点图矩阵
    """
    fig, axes = plt.subplots(figsize = figsize)
    sns.pairplot(
        data = df[cols], 
        kind = "reg", 
        diag_kind = "kde", 
        corner = True
    )
    axes.set_xlabel(xlabel, fontsize = label_fontsize)
    axes.set_ylabel(ylabel, fontsize = label_fontsize)
    axes.set_title(f"{title} 的散点图矩阵", fontsize = title_fontsize)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)



tips = sns.load_dataset("tips")
tips



df = pd.DataFrame({
    "x": tips["total_bill"],
    "y": tips["tip"]
})
df

# 二维散点与统计直方图
sns_reg = sns.jointplot(x = "x", 
                        y = "y",
                        data = df,
                        color = "#D31A8A",
                        kind = "scatter",
                        space = 0,
                        height = 5, 
                        ratio = 5,
                        marginal_kws = {"bins": 20, "rug": False, "hist_kws": {"edgecolor": "k", "color": "#7CBC47", "alpha": 1}}
)
sns_reg.set_axis_labels(xlabel = "total bill", ylabel = "tip");


# 带趋势线的二维散点与统计直方图
sns_reg = sns.jointplot(x = "x", 
                        y = "y",
                        data = df,
                        color = "#7CBC47",
                        kind = "reg",
                        space = 0,
                        height = 5, 
                        ratio = 5,
                        scatter_kws = {"color": "#7CBC47", "alpha": 0.7, "s": 30, "marker": "o"},
                        line_kws = {"color": "#D31A8A", "alpha": 1, "lw": 4},
                        marginal_kws = {"bins": 20, "rug": False, "hist_kws": {"edgecolor": "k", "color": "#7CBC47", "alpha": 1}}
)
sns_reg.set_axis_labels(xlabel = "total bill", ylabel = "tip");


# 二维与一维统计直方图
sns_hex = sns.jointplot(x = "x", 
                        y = "y",
                        data = df,
                        color = "#D31A8A",
                        linewidth = 0.1,
                        kind = "hex",
                        space = 0,
                        height = 5, 
                        ratio = 5,
                        xlim = (0, 60),
                        joint_kws = {"gridsize": 20, "edgecolor": "w"},
                        marginal_kws = {"bins": 20, "rug": False, "hist_kws": {"edgecolor": "k", "color": "#D31A8A", "alpha": 1}}
)
sns_hex.set_axis_labels(xlabel = "total bill", ylabel = "tip");


# 二维与一维核密度估计图
sns_kde = sns.jointplot(x = "x", 
                        y = "y",
                        data = df,
                        color = "#D31A8A",
                        kind = "kde",
                        space = 0
)
sns_kde.plot_joint(plt.scatter, c = "k", s = 10, linewidth = 1, marker = "+")
sns_kde.set_axis_labels(xlabel = "total bill", ylabel = "tip");


# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
