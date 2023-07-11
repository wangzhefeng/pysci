# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : Python 中的环境变量设置
# * Link        : https://mp.weixin.qq.com/s?__biz=Mzg3MjU3NzU1OA==&mid=2247496302&idx=1&sn=a0e2a6b17aceeac9c453e83fb429d262&source=41#wechat_redirect
# **********************************************


# python libraries
import os
import sys
import json


# global variable
GLOBAL_VARIABLE = None


def get_evn_var_normal():
    """
    一般的环境变量设置方法
    # method 1
    ~/language/python_project/pysci/src/(master*)>> VAR1=wangzf python get_env_variables.py
    wangzf

    # method 2
    ~/language/python_project/pysci/src/(master*)>> export VAR1=wangzf
    wangzf
    """
    print(os.environ["VAR1"])


def get_env_var_safe():
    """
    更安全的获取环境变量方法
    ~/language/python_project/pysci/src/(master*)>> python get_env_variables.py
    None
    ~/language/python_project/pysci/src/(master*)>> VAR1=wangzf python get_env_variables.py
    wangzf
    """
    # case 1: 没有设置默认值
    print(os.environ.get("VAR1"))
    # case 2: 设置了默认值
    print(os.environ.get("VAR1", default = "wangzf"))
    # case 3: 同 case 2,但更简单
    print(os.getenv("VAR1", default = "wangzf"))
    # case 4: 其他数据类型的环境变量
    print(int(os.getenv("VAR1", 1)))
    print(float(os.getenv("VAR2", 5.5)))
    print(json.loads(os.getenv("VAR3", '["1", "2"]')))


def get_env_var_by_environs():
    """
    使用 environs 库设置各种类型的环境变量
    Install:
        $ pip install environs
    Usage:
        $ export VAR1=1
        $ export VAR2=2.3
        $ export VAR3=1,2
    """
    from environs import Env
    
    env = Env()
    print(env.int("VAR1", 1))
    print(env.float("VAR2", 5.5))
    print(env.list("VAR3", [1, 2]))





# 测试代码 main 函数
def main():
    # get_evn_var_normal()
    # get_env_var_safe()
    get_env_var_by_environs()


if __name__ == "__main__":
    main()


