# -*- coding: utf-8 -*-
"""
@File          : basic_rule.py
@Date          : 2022-07-26
@Author        : Bairui Zhan
@Contact       : bairui.zhan@yo-i.net
@Version       : 0.1.072614
@Description   : description
@Requirement   : 相关模块版本需求(例如: numpy >= 2.1.0)
"""


import traceback
from .config import input_check_keyword_need, input_check_keyword_default
import re


def write_to_file(content,type,logging_file_name):
    logging_file = open(logging_file_name,type,encoding="utf-8")
    logging_file.write(f"{content}")
    logging_file.close()


def author_check(parameters,check_line,logging_file_name):
    if ("Author" in check_line or "author" in check_line or "AUTHOR" in check_line) and (parameters["_header_check_count"] > 0):
        # TODO 编写者与邮箱有换行问题，之后处理
        logging_file = open(logging_file_name, "a",encoding="utf-8")
        if ":" in check_line:
            logging_file.write(f"此模型代码编写者：{check_line.split(':')[1]}")
        elif "：" in check_line:
            logging_file.write(f"此模型代码编写者：{check_line.split('：')[1]}")
        logging_file.close()
    if ("Email" in check_line or "email" in check_line or "E-mail" in check_line or "Contact" in check_line) and (parameters["_header_check_count"] > 0):
        logging_file = open(logging_file_name, "a",encoding="utf-8")
        if ":" in check_line:
            logging_file.write(f"编写者联系方式：{check_line.split(':')[1]}")
        elif "：" in check_line:
            logging_file.write(f"编写者联系方式：{check_line.split('：')[1]}")
            logging_file.close()


# TODO 如果是流式数据模型检查流程，
def flow_model_check_process(file_name,logging_file_name):
    with open(f"{file_name}.py","r",encoding="utf-8") as f:
        parameters = {}
        parameters['_header_check_count'] = 20
        _method_lines = []
        _method_lines_end_sign = 0
        _doc_lines = ""
        _doc_sign = ""
        for line in f:
            author_check(parameters,line,logging_file_name)
            parameters['_header_check_count'] -= 1
            if _method_lines !=[]:
                if _method_lines_end_sign == 1:
                    _method_final = ""
                    for _line in _method_lines:
                        if 'def' in _line:
                            _method_final = re.sub('\n','',_line)
                        else:
                            _method_final += re.sub('\n','',re.sub(' ','',_line))
                    print(_method_final)
                    # 重置
                    _method_lines = []
                    _method_lines_end_sign = 0
                else:
                    _method_lines.append(line)
                    if ")" in line:
                        _method_lines_end_sign = 1
            elif "def" in line and re.search("def",line).span()[0] == 0:
                _d = line.split("def ")[1]
                _d = _d.split('(')[0]
                try:
                    exec(f"from {file_name.split('.py')[0]} import {_d}")
                    if eval(_d).__doc__ == None:
                        logging_file = open(logging_file_name, "a",encoding="utf-8")
                        logging_file.write(f"{file_name}中,函数{_c}缺少备注.\n")
                        logging_file.close()
                except:
                    _method_lines.append(line)
                    if ")" in line:
                        _method_lines_end_sign = 1
            elif "class" in line and re.search("class",line).span()[0] == 0:
                _method_description = {}
                _c = line.split("class ")[1]
                _c = _c.split('(')[0]
                try:
                    _string = f"from {file_name.split('.py')[0]} import {_c}"
                    exec(_string)
                    for _method in dir(eval(_c)):
                        if _method == "__annotations__":
                            break
                        else:
                            try:
                                exec(f"_method_description['{_method}'] = {_c}.{_method}.__doc__")
                                # exec(f"print({_c}.{_method}.__doc__)")
                                if _method_description[_method] != "":
                                    for _keyword_default in input_check_keyword_default:
                                        if _keyword_default in _method_description[_method]:
                                            logging_file = open(logging_file_name, "a",encoding="utf-8")
                                            logging_file.write(f"{file_name}中,函数{_c}中{_method},{_keyword_default}为默认值，请修改.\n")
                                            logging_file.close()
                                    _count = 0
                                    for _keyword in input_check_keyword_need:
                                        if _keyword in _method_description[_method]:
                                            _count += 1
                                    if _count == 0:
                                        logging_file = open(logging_file_name, "a",encoding="utf-8")
                                        logging_file.write(f"{file_name}中,函数{_c}中{_method}，缺少输入描述，请修改.\n")
                                        logging_file.close()
                                else:
                                    logging_file = open(logging_file_name, "a",encoding="utf-8")
                                    logging_file.write(f"{file_name}中,函数{_c}中{_method},没有描述，请修改.\n")
                                    logging_file.close()
                            except:
                                print(f"读取类{_c}中{_method}失败，请手动检查")
                                traceback.print_exc()
                except:
                    _method_lines.append(line)
                    if ")" in line:
                        _method_lines_end_sign = 1
                        print(_method_lines)
            if "pass" in line:
                if method_wrote_sign == 1:
                    logging_file = open(logging_file_name, "r",encoding="utf-8")
                    print(logging_file.readlines())
                    print(_method_lines_end_sign)
                    _temp_line = logging_file.readlines()[:-1]
                    logging_file.close()
                    logging_file = open(logging_file_name, "w",encoding="utf-8")
                    logging_file.writelines(_temp_line)
                    logging_file.close()
                else:
                    pass
    logging_file = open(logging_file_name, "a",encoding="utf-8")
    logging_file.write(f"流式数据模型{file_name}检查完成。\n")
    logging_file.write(f"==========================================================\n\n")
    f.close()


# TODO 如果是task，判断名称中是否有task然后进入task检查流程，
def task_model_check_process(file_name,logging_file_name):
    print(f"{file_name}是一个定时任务模型")
    logging_file = open(logging_file_name, "a",encoding="utf-8")
    with open(f"{file_name}.py","r",encoding="utf-8") as f:
        _header_check_count = 20
        _count = 0
        _method_lines = []
        _method_lines_end_sign = 0
        _method_final = ""
        _doc_lines = ""
        _doc_sign = 0
        temp_m = ""
        for line in f:
            _header_check_count -= 1
            if _method_lines !=[]:
                if _method_lines_end_sign == 1:
                    for _line in _method_lines:
                        if 'def' in _line:
                            _method_final = re.sub('\n','',_line)
                        else:
                            _method_final += re.sub('\n','',re.sub(' ','',_line))
                    if _doc_sign == 0:
                        if "\"\"\"" in line:
                            _doc_lines += line
                            _doc_sign = 1
                    elif _doc_sign == 1:
                        _doc_lines += line
                        if "\"\"\"" in line:
                            _doc_sign = 2
                    if _doc_sign == 2:
                        # print(_method_final)
                        # print(_doc_lines)
                        if "()" not in _method_final:
                            inputs = _method_final.split("(")[1].split(")")[0].split(",")
                            __count = 0
                            for _input in inputs:
                                if "=" in _input: 
                                    _input = _input.split("=")[0]
                                if _input not in _doc_lines:
                                    if __count == 0:
                                        logging_file.write(f"{temp_m}函数审查问题：\n")
                                        __count = 1
                                    logging_file.write(f"\t输入 {_input} 缺少对应描述。\n")
                        # 重置
                        _method_lines = []
                        _method_lines_end_sign = 0
                        _doc_lines = ""
                        _doc_sign = 0
                        temp_m = ""
                else:
                    _method_lines.append(line)
                    if ")" in line:
                        _method_lines_end_sign = 1
            elif ("Author" in line or "author" in line or "AUTHOR" in line) and (_header_check_count > 0):
                # TODO 编写者与邮箱有换行问题，之后处理
                if ":" in line:
                    logging_file.write(f"此模型代码编写者：{line.split(':')[1]}")
                elif "：" in line:
                    logging_file.write(f"此模型代码编写者：{line.split('：')[1]}")
            elif ("Email" in line or "email" in line or "E-mail" in line) and (_header_check_count > 0):
                if ":" in line:
                    logging_file.write(f"编写者联系方式：{line.split(':')[1]}")
                elif "：" in line:
                    logging_file.write(f"编写者联系方式：{line.split('：')[1]}")
            elif "def" in line and re.search("def",line).span()[0] == 0:
                if "run" in line:
                    pass
                else:
                    _count = 0
                    _d = line.split("def ")[1]
                    _d = _d.split('(')[0]
                    temp_m = _d
                    try:
                        exec(f"from {file_name.split('.py')[0]} import {_d}")
                        if eval(_d).__doc__ == None:
                            logging_file.write(f"{file_name}中,函数{_c}缺少备注.\n")
                    except:
                        print("模型无法直接运行，采用文本读取")
                        _method_lines.append(line)
                        if ")" in line:
                            _method_lines_end_sign = 1
            elif "class" in line and re.search("class",line).span()[0] == 0:
                _method_description = {}
                _count = 0
                _c = line.split("class ")[1]
                _c = _c.split('(')[0]
                try:
                    _string = f"from {file_name.split('.py')[0]} import {_c}"
                    exec(_string)
                    for _method in dir(eval(_c)):
                        if _method == "__annotations__":
                            break
                        else:
                            try:
                                exec(f"_method_description['{_method}'] = {_c}.{_method}.__doc__")
                                # exec(f"print({_c}.{_method}.__doc__)")
                                if _method_description[_method] != "":
                                    for _keyword_default in input_check_keyword_default:
                                        if _keyword_default in _method_description[_method]:
                                            logging_file.write(f"{file_name}中,函数{_c}中{_method},{_keyword_default}为默认值，请修改.\n")
                                    _count = 0
                                    for _keyword in input_check_keyword_need:
                                        if _keyword in _method_description[_method]:
                                            _count += 1
                                    if _count == 0:
                                        logging_file.write(f"{file_name}中,函数{_c}中{_method}，缺少输入描述，请修改.\n")
                                else:
                                    logging_file.write(f"{file_name}中,函数{_c}中{_method},没有描述，请修改.\n")
                            except:
                                print(f"读取类{_c}中{_method}失败，请手动检查")
                                traceback.print_exc()
                except:
                    _method_lines.append(line)
                    if ")" in line:
                        _method_lines_end_sign = 1
                        print(_method_lines)
            if "pass" in line and _count <=2:
                logging_file.close()
                logging_file = open(logging_file_name, "r",encoding="utf-8")
                _temp_line = logging_file.readlines()[:-1]
                logging_file.close()
                logging_file = open(logging_file_name, "w",encoding="utf-8")
                logging_file.writelines(_temp_line)
            _count +=1
    logging_file.write(f"定时任务模型{file_name}检查完成。\n")
    logging_file.write(f"==========================================================\n\n")
    f.close()
    

# TODO其他，通过其他脚本
def other_model_check_process(file_name,logging_file_name):
    print(f"{file_name}是一个通用模型模型")

