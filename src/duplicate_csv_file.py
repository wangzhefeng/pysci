#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time
import datetime
from glob import glob
from sys import argv
from tqdm import trange
import os


# In[90]:


def delete_duplicate(dataframe):
    return dataframe.loc[dataframe.duplicated() == False]


# In[92]:


def find_duplicate(dataframe):
    return dataframe.loc[dataframe.duplicated() == True]


# In[118]:


def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+'创建成功')
        return True
    else:
        print(path+'目录已存在')
        return False

mkdir('./dropped_data')
mkdir('./filtered_data')

PATHS = glob('./*.csv')
for i in trange(len(PATHS)):
    dataframe= pd.read_csv(PATHS[i])
    find_duplicate(dataframe).to_csv('./dropped_data/'+PATHS[i])
    delete_duplicate(dataframe).to_csv('./filtered_data/'+PATHS[i])
if len(glob('./*.csv')) > 0:
    print(f"""已处理{len(PATHS)}个csv数据表，
    其中重复数据丢弃在dropped_data文件夹中，
    过滤后数据放在filtered_data中""")
else:
    print(f'请将本文将放置在数据所在文件夹，现仅支持csv文件表')
    os.removedirs('./dropped_data')
    print('./dropped_data' + "文件夹已删除")
    os.removedirs('./filtered_data')
    print('./filtered_data' + "文件夹已删除")