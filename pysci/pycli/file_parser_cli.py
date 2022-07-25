# -*- coding: utf-8 -*-


# ***************************************************
# * File        : file_parser.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-07-23
# * Version     : 0.1.072301
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


# python libraries
import os
import sys

import argparse


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def file_parser(input_file: str, output_file: str = ""):
    print(f"Processing {input_file}.")
    # TODO
    print("Finished processing.")
    if output_file:
        print(f"Create {output_file}.")


def arg_parser():
    parser = argparse.ArgumentParser(
        "File parser",
        description= "PyParse - The File Processor",
        epilog = "Thank you for choosing PyParse!",
        # add_help = False,
    )
    # group = parser.add_mutually_exclusive_group()
    parser.add_argument("-i", "--infile", help = "Input file for conversion")
    parser.add_argument("-o", "--out", help = "Converted output file")
    args = parser.parse_args()
    if args.infile:
        file_parser(args.infile, args.out)





# 测试代码 main 函数
def main():
    arg_parser()


if __name__ == "__main__":
    main()

