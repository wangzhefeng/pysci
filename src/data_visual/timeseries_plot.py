import os

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from matplotlib import rc
import matplotlib.font_manager as mfm


columns = [
    '日期', 
    '热值(kcal/kg)', 
    '飞灰(%)', 
    '大渣(%)', 
    '排烟温度(℃)', 
    '效率(%)'
    '排烟氧浓度(%)',
]

def timeseries_plot_two_y(df, col_left, col_right, col_left_ylim, col_right_ylim, title, imgpath):
    # config
    plt.style.use("classic")
    plt.style.use("seaborn-whitegrid")
    plt.rcParams['font.sans-serif']= ["Arial Unicode MS"] # 支持中文(macOS)
    mpl.rcParams["axes.unicode_minus"] = False # 解决图像中的 “-” 负号的乱码问题
    rc('mathtext', default = 'regular')  # 支持数学符号

    fig = plt.figure(figsize = (20, 7))
    ax = fig.add_subplot(111)
    line1 = ax.plot_date(df["日期"], df[col_left], linestyle = "solid", color = "#FF4700", label = col_left)
    ax2 = ax.twinx()
    line2 = ax2.plot_date(df["日期"], df[col_right], linestyle = "solid", color = "#009AFF", label = col_right)
    # 图例
    lines = line1 + line2
    labs = [line.get_label() for line in lines]
    ax.legend(lines, labs, loc = 0)
    
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_format)
    
    ax.grid()
    ax.set_xlabel(u"日期")
    ax.set_ylabel(col_left)
    ax.set_ylim(col_left_ylim)
    # ax.set_xticklabels(labels = df["日期"], rotation = 65)
    ax2.set_ylabel(col_right)
    ax2.set_ylim(col_right_ylim)

    plt.title(title)
    
    if imgpath:
        plt.savefig(os.path.join(os.path.dirname(__file__), imgpath))


def timeseries_plot(df, imgpath, title, xlabel, *ylabels):
    """
    matlab plot style
    """
    # config
    plt.style.use("classic")
    plt.style.use("seaborn-whitegrid")
    plt.rcParams['font.sans-serif']= ["Arial Unicode MS"] # 支持中文(macOS)
    mpl.rcParams["axes.unicode_minus"] = False # 解决图像中的 “-” 负号的乱码问题
    rc('mathtext', default = 'regular')  # 支持数学符号
    
    fig, axs = plt.subplots(figsize = (20, 7), sharey = True, tight_layout = True)
    for ylabel in ylabels:
        plt.plot_date(df[xlabel], df[ylabel], linestyle = "solid", label = ylabel)
    
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%Y-%m-%d %H:%M:S')
    plt.gca().xaxis.set_major_formatter(date_format)

    plt.xlabel(xlabel)
    plt.ylabel("")
    plt.xticks(rotation = 45)
    plt.legend()
    plt.ylim(3, 3.5)
    plt.title(title)
    if imgpath:
        plt.savefig(os.path.join(os.path.dirname(__file__), imgpath))


# ------------------------------
# data
# ------------------------------
df_1hour = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "boiler_m4_1h.csv"),
    parse_dates = ["ts"]
)
df_1min = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "boiler_m4_1min.csv"),
    parse_dates = ["ts"]
)
df_5s = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "boiler_m4_5s.csv"),
    parse_dates = ["ts"]
)


timeseries_plot(
    df_1min.loc[(df_1min["ts"] >= "2022-09-23 8:00:00") & (df_1min["ts"] <= "2022-09-23 9:00:00")],
    "figure_1min_08_09.png",
    "时序图",
    "ts",
    "nitrate_lime_feeding_bunker_position"
)
