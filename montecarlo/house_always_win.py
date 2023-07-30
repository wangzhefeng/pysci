# -*- coding: utf-8 -*-

# ***************************************************
# * File        : house_always_win.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-30
# * Version     : 0.1.073019
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
import random

import numpy as np
import matplotlib.pyplot as plt

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def play(total_money, bet_money, total_plays):
    """
    在拥有 total_money 本金，每次下注 bet_money，总共下注 total_plays 次

    Args:
        total_money (_type_): 手中的总金额
        bet_money (_type_): 每次的下注金额
        total_plays (_type_): 玩的次数
    """
    # 玩家下注
    choice = "Even" if np.random.randint(low = 0, high = 2, size = 1) == 0 else "Odd"
    # print(f"You bet on {choice} number")
    if choice == "Even":  # 偶数
        def pick_note():
            """
            生成筹码(chips)数字，
            如果筹码是偶数，并且不是 10 则返回 True
            """
            # 获取 1-100 之间的任意一个随机数
            note = random.randint(1, 100)
            # 检查游戏条件
            if note % 2 != 0 or note == 10:
                return False
            elif note % 2 == 0:
                return True
    elif choice == "Odd":  # 奇数
        def pick_note():
            """
            生成筹码(chips)数字，
            如果筹码是奇数，并且不是 11 则返回 True
            """
            # 获取 1-100 之间的任意一个随机数
            note = random.randint(1, 100)
            # 检查游戏条件
            if note % 2 == 0 or note == 11:
                return False
            elif note % 2 == 1:
                return True
    # 下注次数列表
    num_of_plays = []
    # 钱的变化列表
    money = []
    for play in range(1, total_plays):
        # win
        if pick_note():
            # add the money to funds
            total_money = total_money + bet_money
            # append the play number
            num_of_plays.append(play)
            # append the new fund amount
            money.append(total_money)
        else:
            # add the money to funds
            total_money = total_money - bet_money
            # append the play number
            num_of_plays.append(play)
            # append the new fund amount
            money.append(total_money)
    # 结果可视化
    plt.plot(num_of_plays, money)
    plt.xlabel("Player Money in $")
    plt.ylabel("Number of bets")
    # 最终金额
    final_fund = money[-1]

    return final_fund


def multi_play(num, total_money, bet_money, total_plays):
    """
    模拟多次多次 play
    """
    # 每次模拟的最终金额
    final_funds = []
    for i in range(num):
        ending_fund = play(total_money, bet_money, total_plays)
        final_funds.append(ending_fund)
    print(f"总共模拟了 {num} 次 play.")
    print(f"每次模拟的 play 开始手里的金额为：$10,000.")
    print(f"每次模拟的 play 最后手里的金额为：${final_funds}.")
    print(f"经过 {num} 次模拟，play 一次剩余的平均金额为：${sum(final_funds) / len(final_funds)}")
    plt.show()




# 测试代码 main 函数
def main():
    # final_funds = play(total_money=10000, bet_money=100, total_plays=50)
    # print(final_funds)
    multi_play(num = 1000, total_money=10000, bet_money=100, total_plays=100)

if __name__ == "__main__":
    main()
