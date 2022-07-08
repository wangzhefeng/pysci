# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# **********************************************


# python libraries
import os
import sys
from datetime import date, datetime
import typing
from typing import Dict, List, Tuple, Optional, Sequence, OrderedDict
from pydantic import BaseModel


# global variable
GLOBAL_VARIABLE = None


class Item(BaseModel):
    name: str
    age: int
    is_offer: Optional[bool] = True
    birthday: date
    current: datetime


# 测试代码 main 函数
def main():
    item1: Item = Item(
        name = "wangzf", 
        age = 32, 
        is_offer = True,
        birthday = "1989-10-11",
        current = "2022-01-05 00:00:00"
    )
    print(item1.age)

    func_params = {
        "name": "wangzf", 
        "age": 32, 
        "is_offer": True,
        "birthday": "1989-10-11",
        "current": "2022-01-05 00:00:00"
    }
    item2: Item = Item(**func_params)
    print(item2.name)



if __name__ == "__main__":
    main()

