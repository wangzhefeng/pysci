# -*- coding: utf-8 -*-

# ***************************************************
# * File        : timeseries_plot.py
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
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from matplotlib import rc
import matplotlib.font_manager as mfm
from datetime import datetime
from matplotlib.pyplot import cm
import seaborn as sns
from plotnine import *

# 字体尺寸设置
# plt.rcParams["font.size"] = 10
title_fontsize = 13
label_fontsize = 7

plt.style.use("classic")
plt.style.use("seaborn-whitegrid")
plt.rcParams['font.sans-serif']= ["Arial Unicode MS"] # 支持中文(macOS)
mpl.rcParams["axes.unicode_minus"] = False # 解决图像中的 “-” 负号的乱码问题
rc('mathtext', default = 'regular')  # 支持数学符号

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def timeseries_two_yaxis(df: pd.DataFrame, 
                         col_left: str, 
                         col_right: str, 
                         col_left_ylim: List, 
                         col_right_ylim: List, 
                         figsize: Tuple = (20, 7),
                         title: str = "", 
                         imgpath: str = ""):
    fig = plt.figure(figsize = figsize)
    
    # 左坐标轴
    ax_left = fig.add_subplot(111)
    line1 = ax_left.plot_date(
        df.index, 
        df[col_left], 
        linestyle = "solid", 
        color = "#FF4700", 
        label = col_left
    )
    # 右坐标轴
    ax_right = ax_left.twinx()
    line2 = ax_right.plot_date(
        df.index, df[col_right], 
        linestyle = "solid", 
        color = "#009AFF", 
        label = col_right
    )
    
    # 图例
    lines = line1 + line2
    label_list = [line.get_label() for line in lines]
    ax_left.legend(lines, label_list, loc = 0)
    
    # TODO
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d'))
    
    # TODO
    ax_left.grid()

    # 右坐标轴标签设置
    ax_left.set_xlabel(u"日期")
    ax_left.set_xticklabels(labels = df["日期"], rotation = 65)
    ax_left.set_ylabel(col_left)
    ax_left.set_ylim(col_left_ylim)
    
    # 右坐标轴标签设置
    ax_right.set_xlabel(u"日期")
    ax_right.set_xticklabels(labels = df["日期"], rotation = 65)
    ax_right.set_ylabel(col_right)
    ax_right.set_ylim(col_right_ylim)

    # 标题
    plt.title(title)
    
    if imgpath:
        plt.savefig(os.path.join(os.path.dirname(__file__), imgpath))


def timeseries_plot(df, xcol, ycols: List, show: bool = False, img_file_name: str = None):
    """
    matlab plot style
    """
    fig, axes = plt.subplots(figsize = (30, 7), sharey = True, tight_layout = True)
    for ylabel in ycols:
        plt.plot_date(
            df.index, 
            df[ylabel], 
            linestyle = "solid", 
            label = ylabel
        )
        
        plt.gcf().autofmt_xdate()
        plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter("%Y-%B-%d"))
        
        # x 坐标轴
        plt.xlabel("日期")
        plt.xlim(xlim)
        plt.xticks(rotation = 45)
        # y 坐标轴
        plt.ylabel(ylabel)
        plt.ylim(ylim)
        # 图例
        plt.legend(loc = "best")
        # 标题
        plt.title(ylabel)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(
            os.path.join(os.path.dirname(__file__), f'imgs/{img_file_name}.png'),
            bbox_inches = 'tight', 
            transparent = True)


def plot_timeseries(df: pd.DataFrame, 
                    ycols: List[str], 
                    cate_col: str = None, 
                    figsize: Tuple = (7, 5), 
                    show: bool = False, 
                    img_file_name: str = None):
    """
    时间序列图
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(ycols), figsize = figsize)
    for idx, ycol in enumerate(ycols):
        # ax
        ax = axes[idx] if len(ycols) > 1 else axes
        # 线形图
        if cate_col is not None:
            sns.lineplot(data = df, x = df.index, y = ycol, hue = cate_col, marker = ",", ax = ax)
        else:
            sns.lineplot(data = df, x = df.index, y = ycol, marker = ",", ax = ax)
        
        # x 轴设置
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
        
        # 标题
        ax.set_title(f"{ycol} 在不同 {cate_col} 下的对比图", fontsize = title_fontsize)
    
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(
            os.path.join(os.path.dirname(__file__), f'imgs/{img_file_name}.png'),
            bbox_inches = 'tight', 
            transparent = True)


# TODO
def plot_timeseries_hue(df, xcol = "date", ycol = "value", cate_col = "variable", ):
    base_plot = (
        ggplot(df, aes(x = xcol, y = ycol)) +
            geom_line(aes(group = cate_col, colour = cate_col, fill = cate_col), size = 1) +
            scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
            scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl") + 
            xlab("Year") +
            ylab("Value")
    )
    print(base_plot)

    base_plot = (
        ggplot(df, aes(x = xcol, y = ycol)) +
            geom_line(aes(group = cate_col, colour = cate_col), size = 0.75) +
            geom_area(aes(group = cate_col, fill = cate_col), alpha = 0.55, position = "identity") +
            scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
            scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl") + 
            xlab("Year") +
            ylab("Value")
    )
    print(base_plot)




# 测试代码 main 函数
def main():
    df = pd.read_csv("../data/Line_Data.csv")
    df["date"] = [datetime.strptime(d, "%Y/%m/%d").date() for d in df["date"]]
    melt_df = pd.melt(df, id_vars = ["date"], var_name = "variable", value_name = "value")
    melt_df

if __name__ == "__main__":
    main()
