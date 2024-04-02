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

from utils import plot_prob_result

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def plot_square_circle():
    """
    可视化随机点
    """
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
    
    return myPen


def monter_carlo(num_simu, myPen):
    """
    蒙特卡洛模拟

    Args:
        num_simu (_type_): _description_
        myPen (_type_): _description_
    """
    # 统计在圆形内部和外部的数据点数量
    in_circle = 0
    out_circle = 0
    # 保存 PI 的值
    pi_values = []
    for i in range(num_simu):
        for j in range(1000):
            # 生成随机数字
            x = random.randrange(-100, 100)
            y = random.randrange(-100, 100)
            # 检查数字是否在圆形外部
            if (x ** 2 + y ** 2 > 100 ** 2):
                myPen.color("black")
                myPen.up()
                myPen.goto(x, y)
                myPen.down()
                myPen.dot()
                out_circle = out_circle + 1
            else:
                myPen.color("red") 
                myPen.up()
                myPen.goto(x, y)
                myPen.down()
                myPen.dot()
                in_circle = in_circle + 1
            # 计算 PI 的值
            pi = 4.0 * in_circle / (in_circle + out_circle)
            pi_values.append(pi)
            # 计算误差
            avg_pi_errors = [abs(math.pi - pi) for pi in pi_values]
        print(pi_values[-1])
    # 数据可视化
    plot_prob_result(prob_lists = [pi_values, avg_pi_errors], y_values = [math.pi, 0.0])




# 测试代码 main 函数
def main():
    myPen = plot_square_circle()
    monter_carlo(num_simu = 5, myPen = myPen)

if __name__ == "__main__":
    main()
