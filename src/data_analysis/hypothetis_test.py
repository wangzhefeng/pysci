# -*- coding: utf-8 -*-

# ***************************************************
# * File        : hypothetical_test.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-19
# * Version     : 0.1.071909
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
from typing import List
import warnings

from loguru import logger
import numpy as np
import pandas as pd
from scipy.stats import (
    pearsonr, 
    spearmanr, 
    kendalltau
)

from utils import (
    plot_scatter_reg,
    plot_scatter,
)

warnings.filterwarnings("ignore")

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class CorrHypotheticalTest:
    
    def __init__(self, 
                 df: pd.DataFrame,
                 xcol: np.ndarray,
                 ycol: np.ndarray, 
                 alpha: float = 0.05, 
                 null_info: str = "两个变量相互独立.",
                 alter_info: str = "两个变量可能存在线性相关关系.") -> None:
        # 检验变量的 DataFrame
        self.df = df
        # 检验变量的列名
        self.xcol = xcol
        self.ycol = ycol
        # 检验变量数组
        if df is not None:
            self.xarr = df[xcol].values
            self.yarr = df[ycol].values
        else:
            self.xarr = xcol
            self.yarr = ycol
        # 置信水平
        self.alpha = alpha
        # 打印信息
        self.null_info = null_info
        self.alter_info = alter_info
    
    def _run_test(self, stat, p):
        """
        进行假设检验
        """
        # logger.info(f"检验统计量={stat:.3f}, p Value={p:.3f}, 置信水平={self.alpha}")
        if p > self.alpha:
            # logger.info(f"p Value={p:.3f} > {self.alpha}，不能拒绝原假设，{self.null_info}")
            self.test_res = f"不能拒绝原假设，{self.null_info}"
        elif p < self.alpha:
            # logger.info(f"p Value={p:.3f} < {self.alpha}，拒绝原假设，{self.alter_info}")
            self.test_res = f"拒绝原假设，{self.alter_info}"
    
    def _calc_corr_coef(self, method):
        """
        计算相关系数
        """
        corr_matrix = self.df.corr(method = method)
        self.corr_coef = corr_matrix.loc[self.xcol, self.ycol]
        # logger.info(f"两个变量的相关系数为：{self.corr_coef:.3f}\n")

    def pearson_test(self):
        stat, p = pearsonr(self.xarr, self.yarr)
        self._run_test(stat, p)
        self._calc_corr_coef(method = "pearson")
        
        return stat, p
    
    def spearman_test(self):
        stat, p = spearmanr(self.xarr, self.yarr)
        self._run_test(stat, p)
        self._calc_corr_coef(method = "spearman")
        
        return stat, p
        
    def kendalltau_test(self):
        stat, p = kendalltau(self.xarr, self.yarr)
        self._run_test(stat, p)
        self._calc_corr_coef(method = "kendall")
        
        return stat, p
    
    # def chi_square_test(self):
    #     stat, p = spearmanr(self.x, self.y)
    #     logger.info(f"检验统计量={stat:.3f}, p Value={p:.3f}")
    #     if p > self.alpha:
    #         logger.info(self.null_info)
    #     else:
    #         corr = np.corrcoef(self.x, self.y)
    #         logger.info(self.alter_info)
    #         logger.info(f"两个变量的相关系数为{corr[0, 1]:.3f}")


def corr_test(df: pd.DataFrame, 
              xcols: List[str], 
              ycols: List[str], 
              cate_col: str = None, 
              alpha: float = 0.05, 
              test_log = False):
    """
    批量相关性检验
    """
    # ------------------------------
    # 相关性检验
    # ------------------------------
    res_table = pd.DataFrame()
    for xcol, ycol in zip(xcols, ycols):
        df_test = pd.DataFrame({
            "变量 1": [xcol],
            "变量 2": [ycol],
        })
        # 相关性检验实例
        hypo_test = CorrHypotheticalTest(df, xcol, ycol, alpha = alpha)
        # logger.info("=" * 80)
        # logger.info(f"对变量 {xcol} 与 {ycol} 进行相关性检验...")
        # logger.info("=" * 80)
        
        # Pearson 检验
        if test_log:
            # logger.info("-" * 60)
            logger.info(f"对变量 {xcol} 与 {ycol} 进行 Pearson 相关性检验...")
            logger.info("-" * 55)
            logger.info(f"原假设：随机变量 {xcol} 与 {ycol} 相互独立（或不相关）.")
        stat, p = hypo_test.pearson_test()
        df_test["原假设"] = f"随机变量 {xcol} 与 {ycol} 相互独立（或不相关）."
        df_test["Pearson 检验统计量"] = stat
        df_test["p Value"] = p
        df_test["Pearson 相关系数"] = hypo_test.corr_coef
        df_test["检验结果"] = hypo_test.test_res
        
        '''
        # Spearman 相关性检验
        # logger.info("-" * 60)
        logger.info(f"对变量 {xcol} 与 {ycol} 进行 Spearman 等级相关性检验...")
        logger.info("-" * 55)
        logger.info(f"原假设：随机变量 {xcol} 与 {ycol} 相互独立（或不相关）.")
        stat, p = hypo_test.spearman_test()
        df_test["Spearman 检验统计量"] = stat
        df_test["Spearman p Value"] = p
        df_test["Spearman 相关系数"] = hypo_test.corr_coef
        df_test["Spearman 检验结果"] = hypo_test.test_res

        # Kendall 相关性检验
        # logger.info("-" * 60)
        logger.info(f"对变量 {xcol} 与 {ycol} 进行 Kendall 等级相关性检验...")
        logger.info("-" * 55)
        logger.info(f"原假设：随机变量 {xcol} 与 {ycol} 相互独立（或不相关）.")
        stat, p = hypo_test.kendalltau_test()
        df_test["Kendall 检验统计量"] = stat
        df_test["Kendall p Value"] = p
        df_test["Kendall 相关系数"] = hypo_test.corr_coef
        df_test["Kendall 检验结果"] = hypo_test.test_res
        '''
        res_table = pd.concat([res_table, df_test], axis = 0)
    # ------------------------------
    # 相关关系可视化
    # ------------------------------
    # logger.info(f"变量 {xcol} 与 {ycol} 相关关系可视化...")
    # logger.info("-" * 55)
    # 带拟合曲线的散点图
    plot_scatter_reg(
        df = df, 
        xcols = xcols, 
        ycols = ycols, 
        figsize = (len(xcols) * 5, 5)
    )
    # 类别区分的散点图
    if cate_col is not None:
        plot_scatter(
            df = df,
            xcols = xcols, 
            ycols = ycols, 
            cate_cols = [cate_col] * len(xcols), 
            figsize = (len(xcols) * 5, 5)
        )

    return res_table




# 测试代码 main 函数
def main():
    data1 = [
        0.873, 2.817, 0.121, -0.945, -0.055, 
        -1.436, 0.360, -1.478, -1.637, -1.869
    ]
    data2 = [
        0.353, 3.517, 0.125, -7.545, -0.555, 
        -1.536, 3.350, -1.578, -3.537, -1.579
    ]
    df = pd.DataFrame({
        "dt1": data1,
        "dt2": data2,
    })
    res_table = corr_test(df, xcols = ["dt1"], ycols = ["dt2"])
    print(res_table)
    
if __name__ == "__main__":
    main()
