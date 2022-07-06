# -*- coding: utf-8 -*-

# ***************************************************
# * File        : yaml_demo.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-06
# * Version     : 0.1.070623
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
from typing import Dict
import yaml

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def load_yaml(file_name: str) -> Dict:
    with open(file_name, 'r', encoding = "utf-8") as infile:
        cfg_dict = yaml.load(
            infile, 
            # Loader = yaml.FullLoader
        )
        return cfg_dict




# 测试代码 main 函数
def main():
    pass


if __name__ == "__main__":
    main()

