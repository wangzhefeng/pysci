# -*- coding: utf-8 -*-

# ***************************************************
# * File        : image_plots.py
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

from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


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




# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
