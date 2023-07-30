# -*- coding: utf-8 -*-

# ***************************************************
# * File        : coin_flip.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-23
# * Version     : 0.1.072322
# * Description : description
# * Link        : https://zhuanlan.zhihu.com/p/257196971
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
import random

from utils import plot_prob_result

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def coin_flip() -> int:
    """
    掷硬币

    Returns:
        int: 掷硬币的正反面，1:正面(head), 0:反面(tail)
    """
    return random.randint(0, 1)


def monte_carlo(num_simu: int) -> float:
    """
    Monte Carlo Simulation
    蒙特卡洛模拟验证掷硬币的结果正反两面的概率为 0.5
    
    Args:
        n (int): 掷硬币的次数

    Returns:
        float: 硬币正面或反面的概率
    """
    prob_list = []  # 掷硬币结果为 1 的概率变化过程列表
    num_head = 0  # 模拟结果中掷硬币结果为 1 次数 
    for i in range(num_simu):
        # 掷硬币
        flip_result = coin_flip()
        # 统计掷硬币结果为 1 的次数
        num_head = num_head + flip_result
        # 计算掷硬币结果为 1 的概率
        prob_value = num_head / (i + 1)
        # 将概率放入 res_list
        prob_list.append(prob_value)
    
    # 计算硬币结果为 1 的概率
    prob_head = num_head / num_simu
    # 可视化模拟过程   
    plot_prob_result(prob_list, y_value = 0.5)

    return prob_head




# 测试代码 main 函数
def main():
    res = monte_carlo(num_simu = 50000)
    print(f"Final value: {res}")

if __name__ == "__main__":
    main()
