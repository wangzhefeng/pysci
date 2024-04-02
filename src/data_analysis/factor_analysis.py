# -*- coding: utf-8 -*-

# ***************************************************
# * File        : factor_analysis.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-13
# * Version     : 0.1.071314
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

from loguru import logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import (
    calculate_bartlett_sphericity, 
    calculate_kmo,
)

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def run_factory_analysis(df, hot_stove_idx = None):
    # ------------------
    # 数据
    # ------------------
    if hot_stove_idx is None:
        data = df.drop(
            [
                "manner", "blast_furnace", 
                # "mqxh", "rfl1mqxh", "rfl2mqxh", "rfl3mqxh"
            ], 
            axis = 1
        )
    else:
        data = df.drop(
            [
                "manner", "blast_furnace", 
                # "mqxh", f"rfl{hot_stove_idx}mqxh"
            ], 
            axis = 1
        )
    # ------------------
    # 充分性检验
    # ------------------
    try:
        # Bartlett's Test
        chi_square_value, p_value = calculate_bartlett_sphericity(data)
        logger.info(f"chi_square_value: {chi_square_value}\np_value: {p_value}")  
        # p-value=0, 表明观察到的相关矩阵不是一个identity matrix
        
        # Kaiser-Meyer-Olkin Test
        kmo_all, kmo_model = calculate_kmo(data)
        logger.info(f"kmo_model: {kmo_model}")  # 输出大于 0.6 通过检验

        if p_value != 0.0 or kmo_model < 0.6:
            logger.info(f"数据没有通过检验，不适合因子分析，想想别的办法吧！")
            pass
    except:
        logger.info("没有通过检验，稍后处理该异常，继续进行分析...")
    # ------------------
    # 因子分析
    # ------------------
    fa = FactorAnalyzer(data.shape[1], rotation = None)
    fa.fit(data)
    ev, v = fa.get_eigenvalues()
    # ------------------
    # 崖底碎石图
    # ------------------
    plt.scatter(range(1, data.shape[1] + 1), ev)
    plt.plot(range(1, data.shape[1] + 1), ev)
    plt.title("Scree Plot")
    plt.xlabel("Factory")
    plt.ylabel("Eigenvalue")
    plt.grid()
    plt.show();
    # ------------------
    # 找到隐藏因子
    # ------------------
    # 隐藏因子的数量
    num_hidden_factor = input("num_hidden_factory:")
    fa = FactorAnalyzer(int(num_hidden_factor), rotation = "varimax")
    fa.fit(data)
    # ------------------
    # 载荷矩阵
    # ------------------
    # 计算
    loading_matrix = fa.loadings_
    data_cm = pd.DataFrame(np.abs(loading_matrix), index = data.columns)
    # 可视化
    fig, ax = plt.subplots(figsize = (12, 10))
    sns.heatmap(data_cm, annot = True, cmap = "BuPu", ax = ax)
    ax.tick_params(axis = "x", labelsize = 8)
    ax.set_xlabel("隐藏因子")
    ax.set_ylabel("原始变量")
    ax.set_title("Factory Analysis", fontsize = 10)
    plt.show();
    # ------------------
    # 转换变量
    # ------------------
    # pd.DataFrame(fa.transform(data))




# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
