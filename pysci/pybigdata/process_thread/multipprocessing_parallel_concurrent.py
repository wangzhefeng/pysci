# -*- coding: utf-8 -*-


# ***************************************************
# * File        : utils.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-22
# * Version     : 0.1.072223
# * Description : 用 Python 高效处理大文件
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# system
import os
import sys
_path = os.path.abspath(os.path.dirname(__file__))
if os.path.join(_path, "..") not in sys.path:
    sys.path.append(os.path.join(_path, ".."))
import re
import string

# 多进程、并行、并发
import multiprocessing as mp
from joblib import Parallel, delayed
from tqdm.contrib.concurrent import process_map

# 进度条显示
from tqdm import tqdm

# 数据处理
import pandas as pd
pd.set_option('display.max_columns', None, 'display.max_rows', None)

# 时间评估
from timeit_func import timeit_func 


# 日志标签
LOGGING_LABEL = __file__.split('/')[-1][:-3]
# 数据路径
CURRENT_DIR = os.path.dirname(__file__)
PYSCI_ROOT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
DATA_DIR = os.path.join(PYSCI_ROOT_DIR, "../data/US_Accidents_Dec21_updated.csv")
# CPU 核心数量
N_WORKERS = 2 * mp.cpu_count()
print(f"{N_WORKERS} workers are available.")


@timeit_func
def read_csv(filepath: str):
    df = pd.read_csv(filepath)
    print(f"shape: {df.shape}\n\ncolumn names:\n{df.columns}\n")


@timeit_func
def serial_processing_df(df: pd.DataFrame, 
                         col_name: str, 
                         func) -> pd.DataFrame:
    """
    串行处理 pandas.DataFrame 的某一列

    :param df: _description_
    :type df: pd.DataFrame
    :param col_name: _description_
    :type col_name: str
    :param func: _description_
    :type func
    :return: _description_
    :rtype: pd.DataFrame
    """
    tqdm.pandas()
    df[col_name] = df[col_name].apply(func)
    
    return df


@timeit_func
def serial_processing_df(df: pd.DataFrame, 
                         col_name: str, 
                         func) -> pd.DataFrame:
    """
    串行处理 pandas.DataFrame 的某一列

    :param df: _description_
    :type df: pd.DataFrame
    :param col_name: _description_
    :type col_name: str
    :param func: _description_
    :type func
    :return: _description_
    :rtype: pd.DataFrame
    """
    tqdm.pandas()
    df[col_name] = df[col_name].progress_apply(func)

    return df


@timeit_func
def multip_processing_df(df: pd.DataFrame, 
                         col_name: str, 
                         func) -> pd.DataFrame:
    """
    多进程处理 pandas.DataFrame 的某一列

    :param df: _description_
    :type df: pd.DataFrame
    :param col_name: _description_
    :type col_name: str
    :param func: _description_
    :type func
    :return: _description_
    :rtype: pd.DataFrame
    """
    p = mp.Pool(N_WORKERS)
    df[col_name] = p.map(func, tqdm(df[col_name]))

    return df


@timeit_func
def parallel_processing_df(df: pd.DataFrame, 
                           col_name: str, 
                           func) -> pd.DataFrame:
    
    """
    并行处理 pandas.DataFrame 的某一列

    :return: _description_
    :rtype: _type_
    """
    def parallel_processing(array):
        result = Parallel(n_jobs = N_WORKERS, backend = "multiprocessing")(
            delayed(func)
            (array_col)
            for array_col in tqdm(array)
        )

        return result
    
    df[col_name] = parallel_processing(df[col_name])

    return df


@timeit_func
def parallel_batch_processing_df(df: pd.DataFrame, 
                                 col_name: str,
                                 func) -> pd.DataFrame:
    """
    并行批量处理 pandas.DataFrame 的某一列

    :param df: _description_
    :type df: pd.DataFrame
    :param col_name: _description_
    :type col_name: str
    :param func: _description_
    :type func
    :return: _description_
    :rtype: pd.DataFrame
    """
    def proc_batch(batch):
        """
        批量处理函数

        :param batch: _description_
        :type batch: _type_
        :return: _description_
        :rtype: _type_
        """
        return [
            func(row)
            for row in batch
        ]

    def batch_file(array, n_workers):
        """
        将文件分割成批量数据

        :param array: _description_
        :type array: _type_
        :param n_workers: _description_
        :type n_workers: _type_
        :return: _description_
        :rtype: _type_
        """
        file_len = len(array)
        batch_size = round(file_len / n_workers)
        batches = [
            array[ix:ix+batch_size]
            for ix in tqdm(range(0, file_len, batch_size))
        ]

        return batches
    
    batches = batch_file(array = df[col_name], n_workers = N_WORKERS)
    batch_output = Parallel(n_jobs = N_WORKERS, backend = "multiprocessing")(
        delayed(proc_batch)
        (batch)
        for batch in tqdm(batches)
    )
    df[col_name] = [j for i in batch_output for j in i]

    return df


@timeit_func
def tqdm_concurrent_processing_df(df: pd.DataFrame, 
                                  col_name: str,
                                  func) -> pd.DataFrame:
    batch = round(len(df) / N_WORKERS)
    df[col_name] = process_map(
        func, 
        df[col_name],
        max_workers = N_WORKERS,
        chunksize = batch,
    )

    return df




# 测试代码 main 函数
def main():
    read_csv(DATA_DIR)

if __name__ == "__main__":
    main()

