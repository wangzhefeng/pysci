# -*- coding: utf-8 -*-


# ***************************************************
# * File        : main.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-06
# * Version     : 0.1.070623
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys
_path = os.path.abspath(os.path.dirname(__file__))
if os.path.join(_path, "..") not in sys.path:
    sys.path.append(os.path.join(_path, ".."))

from pyyaml import load_yaml

CFG_DIR = os.path.dirname(__file__)





# 测试代码 main 函数
def main():
    cfg = load_yaml(os.path.join(CFG_DIR, "cfg.yml"))
    print(cfg)


if __name__ == "__main__":
    main()

