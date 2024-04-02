# -*- coding: utf-8 -*-

# ***************************************************
# * File        : bar_plots.py
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
from matplotlib.pyplot import cm
import seaborn as sns
from plotnine import *
import joypy


# 字体尺寸设置
# plt.rcParams["font.size"] = 10
title_fontsize = 13
label_fontsize = 7

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def bar_plot(data: pd.DataFrame, xcol: str, ycol: str, theme: str = "ggplot"):
    """
    柱状图
    
    Args:
        data (pd.DataFrame): 数据
        xcol (str): 类别型变量
        ycol (str): 类别型变量数据统计量
        theme (str, optional): 主题. Defaults to "ggplot".
    """
    # 数据预处理
    sort_data = data.sort_values(by = ycol, ascending = False)
    sort_data[xcol] = pd.Categorical(sort_data[xcol], ordered = True, categories = sort_data[xcol])

    # 绘图
    if theme == "ggplot":
        base_plot = (
            ggplot(sort_data, aes(xcol, ycol)) +
            geom_bar(stat = "identity", width = 0.8, colour = "black", size = 0.25, fill = "#FC4E07", alpha = 1)
        )
        print(base_plot)
    elif theme == "mpl":
        fig = plt.figure(figsize = (6, 7), dpi = 70)
        plt.bar(sort_data[xcol], sort_data[ycol], width = 0.8, align = "center", label = xcol)
        plt.title(f"柱状图")
        plt.show();


def bar_plot(df, x, y, categorical):
    fig, ax = plt.subplots(figsize = (20, 5))
    palette = sns.color_palette("mako_r", 4)
    a = sns.barplot(x = "month", y = "Sales", hue = "year", data = df)
    a.set_title("Store %s Data" % y, fontsize = 15)
    plt.legend(loc = "upper right")
    plt.show()


def bar_plots(df, x, y, xlabel, ylabel, title, nrows):
    fig,(ax1,ax2,ax3,ax4)= plt.subplots(nrows=nrows)
    fig.set_size_inches(20,30)
    for ax in [ax1,ax2,ax3,ax4]:
        sns.barplot(data = df, x = x,y = y, ax = ax)
        ax.set(xlabel = xlabel, ylabel = ylabel)
        ax.set_title(title, fontsize=15)


def hist_plot(df, *xlabels, xlim = None, imgpath = None):
    """
    pandas plot style
    """
    fig, axs = plt.subplots(figsize = (10, 7), sharey = True, tight_layout = True)
    for xlabel in xlabels:
        df[xlabel].plot(kind = "hist", bins = 20, color = "steelblue", edgecolor = "black", density = True, label = "Histogram")
        df[xlabel].plot(kind = "kde", color = "red", label = "KDE")
        # kwargs = dict(histtype = "", alpha = 0.3, normed = True, bins = 40)
        # plt.hist(data, **kwargs)
        # counts, bin_edges = np.histogram(data, bins=5)
        plt.xlabel("%s" % xlabel)
        plt.ylabel("Count")
        plt.title("%s Histogram" % xlabel)
    
    if xlim:
        plt.xlim(xlim[0], xlim[1])
    plt.legend()
    
    if imgpath:
        plt.savefig(imgpath)
    plt.show();


def histogram_plot(df, row, col, categorical, imgpath = None):
    """
    分面直方图
    """
    gird = sns.FacetGrid(df, row, col, margin_titles = True)
    gird.map(plt.hist, categorical, bins = np.linspace(0, 40, 15))


def plot_distributed(df: pd.DataFrame, 
                     xcols: List[str], 
                     cate_cols: List[str], 
                     figsize: Tuple = (5, 5), 
                     show: bool = False, 
                     img_file_name: str = None):
    """
    绘制连续变量分布图

    Args:
        df (pd.DataFrame): _description_
        xcols (List[str]): _description_
        cate_cols (List[str]): _description_
        figsize (Tuple, optional): _description_. Defaults to (5, 5).
        show (bool, optional): _description_. Defaults to False.
        img_file_name (str, optional): _description_. Defaults to None.
    """
    fig, axes = plt.subplots(nrows = 1, ncols = len(xcols), figsize = figsize)
    for idx, xcol, cate_col in zip(range(len(xcols)), xcols, cate_cols):
        # ax
        ax = axes[idx] if len(xcols) > 1 else axes
        # 绘图
        if cate_col is not None:
            sns.histplot(data = df, x = xcol, hue = cate_col, kde = True, ax = ax)
        else:
            sns.histplot(data = df, x = xcol, kde = True, ax = ax)
        ax.set_xlabel(xcol, fontsize = label_fontsize)
        ax.set_title(f"{xcol} 分布直方图", fontsize = title_fontsize)
    # 图像显示
    if show:
        plt.show()
    # 图像保存
    if img_file_name is not None:
        fig.get_figure().savefig(f'imgs/{img_file_name}.png', bbox_inches = 'tight', transparent = True)



def plot_histogram(df):
    base_plot = (
        ggplot(df, aes(x = "value", fill = "class")) +
            geom_histogram(bins = 30, alpha = 1, colour = "black", size = 0.2) +
            facet_grid("class~") +
            scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl") +
            theme_light()
    )
    print(base_plot)


    base_plot = (
        ggplot(df, aes(x = "value", fill = "class")) +
            geom_density(alpha = 1) +
            facet_grid("class~") +
            scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl") +
            theme_light()
    )
    print(base_plot)



(ggplot(df, aes(x = "MXSPD", fill = "Location")) +
    geom_histogram(binwidth = 1, alpha = 0.55, colour = "black", size = 0.25) +
    scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl")
)

(ggplot(df, aes(x = "MXSPD", fill = "Location")) +
     geom_density(bw = 1, alpha = 0.55, colour = "black", size = 0.25) +
     scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl")
)


Categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = pd.api.types.CategoricalDtype(categories = Categories, ordered = True)
df["Month"] = df["Month"].astype(month)

fig, axes = joypy.joyplot(
    df, 
    column = ["Mean.Temperature..F."], 
    by = "Month", 
    ylim = "own", 
    colormap = cm.Spectral, 
    alpha = 0.9, 
    figsize = (6, 5)
)
plt.xlabel("Mean Temperature")
plt.ylabel("Month")



def variable_width_column():
    """
    不等宽柱状图
    """
    base_plot = (
        ggplot(mydata) +
            geom_rect(aes(xmin = "xmin", xmax = "xmax", ymin = 0, ymax = "ARPU", fill = "Name"), colour = "black", size = 0.25) +
            geom_text(aes(x = "label", y = "ARPU + 3", label = "ARPU"), size = 10, colour = "black") +
            geom_text(aes(x = "label", y = -4, label = "Name"), size = 7, colour = "black") +
            scale_fill_hue(s = 0.90, l = 0.65, h = 0.0417, color_space = "husl")
    )
    base_plot


# 棒棒糖图
# data
df = pd.read_csv("../data/DotPlots_Data.csv")
df["sum"] = df.iloc[:, 1:3].apply(np.sum, axis = 1)
df = df.sort_values(by = "sum", ascending = True)
City_type = pd.api.types.CategoricalDtype(categories = df["City"], ordered = True)
df["City"] = df["City"].astype(City_type)

# plot
base_plot = (
    ggplot(df, aes("sum", "City")) + 
        geom_segment(aes(x = 0, xend = "sum", y = "City", yend = "City")) +
        geom_point(shape = "o", size = 3, color = "black", fill = "#FC4E07")

)
print(base_plot)



# 克利夫兰图
# data
df = pd.read_csv("../data/DotPlots_Data.csv")
df["sum"] = df.iloc[:, 1:3].apply(np.sum, axis = 1)
df = df.sort_values(by = "sum", ascending = True)
City_type = pd.api.types.CategoricalDtype(categories = df["City"], ordered = True)
df["City"] = df["City"].astype(City_type)

# plot
base_plot = (
    ggplot(df, aes("sum", "City")) + 
        geom_point(shape = "o", size = 3, color = "black", fill = "#FC4E07")
)
print(base_plot)



# 哑铃图
# data
df = pd.read_csv("../data/DotPlots_Data.csv")
df = df.sort_values(by = "Female", ascending = True)
City_type = pd.api.types.CategoricalDtype(categories = df["City"], ordered = True)
df["City"] = df["City"].astype(City_type)
mydata = pd.melt(df, id_vars = "City")
base_plot = (
    ggplot(mydata, aes(x = "value", y = "City")) + 
        geom_line(aes(group = "City")) +
        geom_point(aes(fill = "variable"), shape = "o", size = 3, color = "black") +
        scale_fill_manual(values = ("#00AFBB", "#FC4E07", "#36BED9"))
)
print(base_plot)





# 测试代码 main 函数
def main():
    bar_data = pd.DataFrame({
        "Cut": ["Fair", "Good", "Very Good", "Premium", "Ideal"],
        "Price": [4300, 3800, 3950, 4700, 3500],
    })
    bar_plot(data = bar_data, xcol = "Cut", ycol = "Price", theme = "mpl")
    
    
    df = pd.read_csv("../data/Distribution_Data.csv")
    classes = pd.api.types.CategoricalDtype(categories=["n", "s", "k", "mm"], ordered = True)
    df["class"] = df["class"].astype(classes)
    df
    
    normal_data = np.random.normal(3, 1, size = 100)
    normal_data
    
    df = pd.read_csv("../data/Hist_Density_Data.csv")
    df
    
    
    df = pd.read_csv("../data/lincoln_weather.csv")
    df
    
    # 不等宽柱状图
    mydata = pd.DataFrame({
        "Name": ["Project 1", "Project 2", "Project 3", "Project 4", "Project 5"],
        "Scale": [35, 30, 20, 10, 15],
        "ARPU": [56, 37, 63, 57, 59]
    })
    mydata["xmin"] = 0
    for i in range(1, 5):
        mydata["xmin"][i] = np.sum(mydata["Scale"][0:i])
    mydata["xmax"] = 0
    for i in range(0, 5):
        mydata["xmax"][i] = np.sum(mydata["Scale"][0:i+1])
    mydata["label"] = 0
    for i in range(0, 5):
        mydata["label"][i] = np.sum(mydata["Scale"][0:i+1]) - mydata["Scale"][i] / 2
    mydata

if __name__ == "__main__":
    main()
