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


from fileinput import filename
import traceback
from .config import *
import re
from enum import Enum


class ModelType(Enum):
    """
    模型类型
    """
    flow = 1
    """
    流式数据模型 1
    """
    task = 2
    """
    定时任务 2
    """
    other = 3
    """
    通用脚本 3
    """


def write_to_file(content,type,logging_file_name):
    logging_file = open(logging_file_name,type,encoding="utf-8")
    logging_file.write(f"{content}")
    logging_file.close()


# 作者查询
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
    parameters['_header_check_count'] -= 1
    return parameters


# TODO 主体查询
def main_check(parameters,check_line,logging_file_name):
    if ("class" in check_line and re.search("class",check_line).span()[0] == 0):
        parameters["upper"] = (check_line.split('(')[0]).split('class ')[1]
        parameters["upper_type"] = "class"
        if parameters.get("check_sign",0) == 1:
            write_to_file(f"{parameters['current_name']}没有备注\n","a",logging_file_name)
        parameters["current_name"] = (check_line.split('(')[0]).split('class ')[1]
        if "(" not in check_line:
            pass
        else:
            if (check_line.split("(")[1]).split(")")[0] == "simple.SimpleClassTemplate" and (parameters["model_type"] == ModelType["flow"]):
                parameters["check_sign"] = 0
                if parameters['file_name'] == (check_line.split('(')[0]).split('class ')[1]:
                    pass
                else:
                    write_to_file(f"{(check_line.split('(')[0]).split('class ')[1]}数孪类与文件名不符，请确认修改。\n","a",logging_file_name)
            else:
                parameters["type"] = "class"
                parameters["check_sign"] = 1
                parameters["args"] = []
                if "," in (check_line.split('(')[1]).split(')')[0]:
                    for arg in re.sub(" ","",(check_line.split(')')[0]).split('(')[1]).split(","):
                        if ":" in arg:
                            parameters["args"].append(arg.split(":")[0])
                        else:
                            parameters["args"].append(arg)
                else:
                    parameters["args"] = [re.sub(" ","",(check_line.split(')')[0]).split('(')[1])]
    # TODO 如果 class 有，但是不是开头的，建议吧这个类写到函数外部。
    elif "class" in check_line and re.search("class",check_line).span()[0] == 4 and re.sub(" ","",check_line.split("class")[0]) == "":
        if parameters.get("check_sign",0) == 1:
            if parameters["upper_type"] == "class":
                write_to_file(f"类{parameters['upper']}中{parameters['current_name']}没有备注\n","a",logging_file_name)
            else:
                write_to_file(f"函数{parameters['upper']}中{parameters['current_name']}没有备注\n","a",logging_file_name)
        if re.sub(" ","",check_line.split("class")[0]) == "" and "class " in check_line:
            parameters["current_name"] = (check_line.split('(')[0]).split('class ')[1]
            write_to_file(f"请将{(check_line.split('(')[0]).split('class ')[1]}类修改到外层\n","a",logging_file_name)
            parameters["check_sign"] = 0
    # TODO 再 判断是否有函数
    if "def" in check_line:
        if re.search("def",check_line).span()[0] == 0:
            parameters["upper"] = (check_line.split('(')[0]).split('def ')[1]
            parameters["upper_type"] = "def"
            if parameters.get("check_sign",0) == 1:
                write_to_file(f"函数{parameters['current_name']}没有备注\n","a",logging_file_name)
            parameters["type"] = "def"
            # TODO 处理函数多行的问题
            if ")" in check_line:
                parameters["current_name"] = (check_line.split('(')[0]).split('def ')[1]
                
                parameters["check_sign"] = 1
                parameters["args"] = []
                if "," in (check_line.split('(')[1]).split(')')[0]:
                    for arg in re.sub(" ","",(check_line.split(')')[0]).split('(')[1]).split(","):
                        if ":" in arg:
                            parameters["args"].append(arg.split(":")[0])
                        else:
                            parameters["args"].append(arg)
                else:
                    parameters["args"] = [re.sub(" ","",(check_line.split(')')[0]).split('(')[1])]
            else:
                parameters['args_not_finish_sign'] = 1
                parameters['line_temp_save'] = check_line
        elif re.search("def",check_line).span()[0] == 4:
            if parameters.get("check_sign",0) == 1:
                if parameters["upper_type"] == "class":
                    write_to_file(f"类{parameters['upper']}中函数{parameters['current_name']}没有备注\n","a",logging_file_name)
                else:
                    write_to_file(f"函数{parameters['upper']}中函数{parameters['current_name']}没有备注\n","a",logging_file_name)
            parameters["type"] = "def"
            # TODO 处理函数多行的问题
            if ")" in check_line:
                parameters["current_name"] = (check_line.split('(')[0]).split('def ')[1]
                
                parameters["check_sign"] = 1
                parameters["args"] = []
                if "," in (check_line.split('(')[1]).split(')')[0]:
                    for arg in re.sub(" ","",(check_line.split(')')[0]).split('(')[1]).split(","):
                        if ":" in arg:
                            parameters["args"].append(arg.split(":")[0])
                        else:
                            parameters["args"].append(arg)
                else:
                    parameters["args"] = [re.sub(" ","",(check_line.split(')')[0]).split('(')[1])]
            else:
                parameters['args_not_finish_sign'] = 1
                parameters['line_temp_save'] = check_line
        elif re.search("def",check_line).span()[0] == 8:
            if re.sub(" ", "",check_line.split("def")[0]) != "":
                print(check_line)
                write_to_file(f"请将{(check_line.split('(')[0]).split('def ')[1]}函数修改到外层\n","a",logging_file_name)
                parameters["check_sign"] = 0
    if parameters.get("args_not_finish_sign",0) == 1:
        parameters["args_not_finish_sign"] =2
    elif parameters.get("args_not_finish_sign",0) == 2:
        if ")" in check_line:
            parameters['line_temp_save'] += check_line
            if parameters.get("type", "") == "def":
                parameters["current_name"] = (parameters['line_temp_save'].split('(')[0]).split('def ')[1]
            print(f"current_name:{parameters['current_name']}")
            # parameters["type"] = "def"
            parameters["check_sign"] = 1
            parameters["args"] = []
            _temp_line =  (parameters['line_temp_save'].split('(')[1]).split(')')[0]
            if "," in _temp_line:
                for arg in re.sub(" ","",re.sub("\n","",_temp_line)).split(","):
                    if ":" in arg:
                        parameters["args"].append(arg.split(":")[0])
                    else:
                        parameters["args"].append(arg)
            parameters['args_not_finish_sign'] = 0
        else:
            parameters['line_temp_save'] += check_line
    # TODO 查找当前 函数 doc
    if parameters.get("check_sign") == 0:
        pass
    else:
        if parameters.get("doc_sign",0) == 0:
            if "\"\"\"" in check_line:
                parameters["doc_string"] = f"{check_line}"
                if re.search("\"\"\"",check_line[re.search("\"\"\"",check_line).span()[1]:]) ==None:
                    parameters['doc_sign'] = 1
                else:
                    parameters['doc_sign'] = 2
        elif parameters.get("doc_sign",0) == 1:
            parameters["doc_string"] += f"{check_line}"
            if "\"\"\"" in check_line:
                parameters['doc_sign'] = 2
        

    return parameters


def report_process(parameters,check_line,logging_file_name):
    if parameters.get('doc_sign',0) == 2 and parameters.get("check_sign",0) == 1:
        for _keyword_default in input_check_keyword_default:
            if _keyword_default in parameters["doc_string"]:
                if parameters["upper"] == parameters["current_name"]:
                    write_to_file(f"{parameters['upper']}，{_keyword_default}为默认值，请修改.\n","a",logging_file_name)
                else:
                    write_to_file(f"{parameters['upper']}中{parameters['current_name']}，{_keyword_default}为默认值，请修改.\n","a",logging_file_name)
        _count = 0
        for _keyword in input_check_keyword_need:
            if _keyword in parameters["doc_string"]:
                _count += 1
        if _count == 0:
            if parameters["upper"] != parameters['current_name']:
                write_to_file(f"{parameters['upper']}中,{parameters['current_name']}缺少输入描述，请修改.\n","a",logging_file_name)
            else:
                write_to_file(f"{parameters['upper']}缺少输入描述，请修改.\n","a",logging_file_name)
        for i in parameters["args"]:
            if i not in parameters["doc_string"]:
                if parameters["upper"] != parameters['current_name']:
                    write_to_file(f"{parameters['upper']}中,{parameters['current_name']}缺少{i}描述，请修改.\n","a",logging_file_name)
                else:
                    write_to_file(f"{parameters['upper']}缺少{i}描述，请修改.\n","a",logging_file_name)
        del_list = []
        for key,value in parameters.items():
            # print(f"{key}:{value}")
            if key not in ["upper","upper_type","model_type","current","file_name","start_length","total_lines","_header_check_count"]:
                del_list.append(key)
        for i in del_list:
            del parameters[i]
    # TODO 最后一行
    if parameters.get("final_sign",0) ==1:
        # 该判断的都要判断完成
        print("最后行的处理")
    # 对当前parameters 进行整理输出
    return parameters


# 模型检查流程，
def model_check_process(file_name,logging_file_name,model_type,flow_model_list=[],task_model_list=[],path=""):
    if file_name == "code_review" or "code_review" == path:
        pass
    else:
        parameters = {}
        parameters["model_type"] = model_type
        parameters["current"] = 1
        parameters['file_name'] = file_name
        if model_type == ModelType["flow"]:
            parameters["start_length"] = len(f"┏━━━━━━━━数孪模型{file_name}流式数据模型审查━━━━━━━━┓") + 8
            write_to_file(f"┏━━━━━━━━数孪模型{file_name}流式数据模型审查━━━━━━━━┓\n","a",logging_file_name)
            if (flow_model_list != []) and (file_name not in flow_model_list):
                write_to_file(f"当前数孪模型{file_name}未在项目配置中，请检查。\n","a",logging_file_name)
            
        elif model_type == ModelType["task"]:
            parameters["start_length"] = len(f"┏━━━━━━━━task模型{file_name}定时任务模型审查━━━━━━━━┓") + 6
            write_to_file(f"┏━━━━━━━━task模型{file_name}定时任务模型审查━━━━━━━━┓\n","a",logging_file_name)
            if (task_model_list !=[]) and (file_name not in task_model_list):
                write_to_file(f"当前数孪模型{file_name}未在项目配置中，请检查。\n","a",logging_file_name)
        elif model_type == ModelType["other"]:
            parameters["start_length"] = len(f"┏━━━━━━━━{path}通用其他模型{file_name}审查━━━━━━━━┓") + 5
            print(parameters["start_length"])
            write_to_file(f"┏━━━━━━━━{path}通用其他模型{file_name}审查━━━━━━━━┓\n","a",logging_file_name)
            print("其他通用模型审查starting")
        else:
            print("单文件模型审查出错，审查类型有误，请联系脚本维护者。")
        if path == "":
            file_name_with_path = file_name
        else:
            file_name_with_path = f"{path}/{file_name}"
        f = open(f"{file_name_with_path}.py","r",encoding="utf-8")
        parameters['total_lines'] = len(f.readlines())
        f.close
        f = open(f"{file_name_with_path}.py","r",encoding="utf-8")
        print(parameters)
        parameters['_header_check_count'] = header_check_count
        line = f.readline()
        while line:
            if parameters["current"] != parameters['total_lines']:
                parameters["final_sign"] = 0
            else:
                parameters["final_sign"] = 1
            # 作者查询
            if parameters['_header_check_count'] > 0 :
                parameters.update(author_check(parameters,line,logging_file_name))
            
            # TODO 主体查询
            parameters.update(main_check(parameters,line,logging_file_name))
            parameters.update(report_process(parameters,line,logging_file_name))
            parameters["current"] += 1
            line = f.readline()
        f.close()
        if model_type == ModelType["flow"]:
        # NOTE End of the process
            write_to_file(f"流式数据模型{file_name}检查完成。\n","a",logging_file_name)
            _end_length = parameters.get("start_length",30)
            write_to_file("┗"+"━"*_end_length+"┛"+"\n\n","a",logging_file_name)
        elif model_type == ModelType["task"]:
        # NOTE End of the process
            write_to_file(f"定时任务模型{file_name}检查完成。\n","a",logging_file_name)
            _end_length = parameters.get("start_length",30)
            write_to_file("┗"+"━"*_end_length+"┛"+"\n\n","a",logging_file_name)
        elif model_type == ModelType["other"]:
        # NOTE End of the process
            write_to_file(f"通用函数模型{file_name}检查完成。\n","a",logging_file_name)
            _end_length = parameters.get("start_length",30)
            write_to_file("┗"+"━"*_end_length+"┛"+"\n\n","a",logging_file_name)

