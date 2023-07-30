# -*- coding: utf-8 -*-

# ***************************************************
# * File        : square_circle_pi.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-23
# * Version     : 0.1.072323
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
import math
import turtle
import random

import matplotlib.pyplot as plt
from utils import plot_prob_result

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_square_circle():
    # 可视化随机点
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    
    # 画一个正方形
    myPen.up()
    myPen.setposition(-100, -100)
    myPen.down()
    myPen.fd(200)
    myPen.left(90)
    myPen.fd(200)
    
    myPen.left(90)
    myPen.fd(200)
    myPen.left(90)
    myPen.fd(200)
    myPen.left(90)
    
    # 画一个圆形
    myPen.up()
    myPen.setposition(0, -100)
    myPen.down()
    myPen.circle(100)


def monter_carlo(num_simu):
    # 统计在圆形内部和外部的数据点数量
    in_circle = 0
    out_circle = 0
    # 保存 PI 的值
    pi_values = []
    for i in range(num_simu):
        for j in range(1000):
            # 生成随机数字
            x = random.randrange(-100, 100)
            y = random.randragne




# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
