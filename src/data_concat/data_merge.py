# -*- coding: utf-8 -*-


# ***************************************************
# * File        : data_merge.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-08-10
# * Version     : 0.1.081015
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import pandas as pd


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def read_data(data_file, dt_col_name):
    """
    读取数据
    """
    data = pd.read_csv(data_file)
    if len(data) != 0:
        data[dt_col_name] = pd.to_datetime(data[dt_col_name])
        return data
    else:
        return None


def write_data(data, data_path, data_file_name):
    """
    保存数据
    """
    data.to_csv(os.path.join(data_path, data_file_name), index = False)


def concat_data(data_path, data_files, result_filename, dt_col_name, is_need_date_col):
    """
    数据合并
    """
    # 数据合并 
    df = pd.DataFrame({})
    for data_file in data_files:
        data = read_data(data_file, dt_col_name)
        if data is not None:
            df = pd.concat([df, data], axis = 0, ignore_index = True)
    # 数据排序
    df = df.sort_values(by = [dt_col_name])
    # 增加日期列
    if is_need_date_col:
        df["date"] = [d.date() for d in df[dt_col_name]]
    # 数据保存
    df.reset_index(drop = True, inplace = True)
    write_data(df, data_path, result_filename)


def merge_data(data_path, data_files, result_filename, dt_col_name, date_start, date_end, date_freq):
    """
    数据连接
    """
    df = pd.DataFrame({
        dt_col_name: pd.date_range(start = date_start, end = date_end, freq = date_freq)
    })
    for data_file in data_files:
        data = read_data(data_file, dt_col_name)
        df = df.merge(data, on = [dt_col_name], how = "left")
    # 数据填充
    df = df.fillna(method = "ffill")
    df = df.fillna(method = "bfill")
    # 数据保存
    df.reset_index(drop = True, inplace = True)
    write_data(df, data_path, result_filename)




def main():
    pass

if __name__ == "__main__":
    main()

