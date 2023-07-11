# -*- coding: utf-8 -*-


# ***************************************************
# * File        : data_merge_air_power.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-09-17
# * Version     : 0.1.091714
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import glob
import logging

import pandas as pd
from data_merge import concat_data


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def concat_download_data(data_file_path, data_result_path, result_file, dt_col_name = "ts"):
    """
    每台锅炉下载数据合并
    """
    # ------------------------------
    # 数据文件路径
    # ------------------------------
    data_files = glob.glob(data_file_path + '/' + "*.csv")
    logging.error(f"data_files={data_files}")
    # ------------------------------
    # 数据合并
    # ------------------------------
    concat_data(
        data_path = data_result_path,
        data_files = data_files,
        result_filename = result_file,
        dt_col_name = dt_col_name,
        is_need_date_col = False,
    )
    logging.error(f"concat_data finished.")


def data_process():
    root_path = os.path.join(os.path.dirname(__file__), "result")
    data_path = os.path.join(root_path, "yanhua_data")
    result_path = os.path.join(data_path, "result")
    # 配置信息
    boiler_info = {
        "boiler_m4": "boiler_m5_df.csv",
    }
    # ------------------------------
    # 下载的数据处理
    # ------------------------------
    for file_download_path, res_file_name in boiler_info.items():
        concat_download_data(
            data_file_path = os.path.join(data_path, file_download_path),
            data_result_path = result_path,
            result_file = res_file_name,
            dt_col_name = "ts"
        )




# 测试代码 main 函数
def main():
    data_process()


if __name__ == "__main__":
    main()

