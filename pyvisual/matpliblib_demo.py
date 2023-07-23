# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# **********************************************


# python libraries
from os import read
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


# global variable
GLOBAL_VARIABLE = None


def a_simple_example():
    # method 1
    fig, ax = plt.subplots()
    ax.plot(
        [1, 2, 3, 4],
        [1, 4, 2, 3]
    )
    # method 2
    # plt.plot(
    #     [1, 2, 3, 4],
    #     [1, 4, 2, 3]
    # )
    plt.show()


def read_image():
    # 将图像转换为 numpy array
    path = "/Users/zfwang/machinelearning/mlproj/src/data_visualization/python/stinkbug.png"
    img = mpimg.imread(path)
    # print(img)
    # print(img.shape)
    
    # 将 numpy 数组绘制为图像
    # imgplot = plt.imshow(img)
    
    # 伪彩色
    # lum_img = img[:, :, 0]
    # plt.imshow(lum_img)
    # plt.imshow(lum_img, cmap = "hot")

    # imgplot = plt.imshow(lum_img)
    # imgplot.set_cmap("nipy_spectral")

    # plt.colorbar()

    # plt.hist(lum_img.ravel(), bins = 256, range = (0.0, 1.0), fc = "k", ec = "k")
    # imgplot = plt.imshow(lum_img, clim = (0.0, 0.7))
    # plt.show()


def image_interplo():
    path = "/Users/zfwang/machinelearning/mlproj/src/data_visualization/python/stinkbug.png"
    img = Image.open(path)
    img.thumbnail((64, 64), Image.ANTIALIAS)
    # imgplot = plt.imshow(img)
    # imgplot = plt.imshow(img, interpolation = "nearest")
    imgplot = plt.imshow(img, interpolation = "bicubic")
    plt.show()


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
    # a_simple_example()
    # read_image()
    # image_interplo()
    lifecycle_of_a_plot()


    


if __name__ == "__main__":
    main()

