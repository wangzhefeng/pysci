import os
import platform
import re
plat = platform.system().lower()
import getopt
import sys
from enum import Enum
import json
import time
import yaml
from code_review.basic_rule import *


# TODO 询问是否对单个脚本进行排查，如果不是，对全部脚本进行排查
dir_path = os.path.abspath("")
SINGLE_FILE_NAME_WITH_PATH = None
SCRIPT_METHOD = None
SINGLE_FILE_METHOD = None
folder_path = f"./code_review/report"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
logging_file_path = os.path.join(folder_path,"项目代码规范审查报告.txt")
write_to_file(f"报告时间:{time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))}\n\n","w",logging_file_path)

FLOW_MODELS = []
try:
    with open(os.path.join(dir_path, "../../cfg/config.json"),encoding="utf-8") as load_f:
        DM_CONFIG = json.load(load_f)
    for _layer in DM_CONFIG["model_hierarchy"]:
        for _class in _layer["models"]:
            FLOW_MODELS.append(_class.split("}")[1])
    with open(os.path.join(dir_path, "../../dm/models.yaml"), encoding="UTF-8") as load_f:
        TASK_CONFIG = yaml.load(load_f, Loader=yaml.SafeLoader)
except:
    print("当前未能打开项目配置文件/cfg/config.json，部分检查功能未开启，")
    print("推荐在项目/dm/\{pacakgename\}下运行本脚本。")

TASK_MODELS = []
for _task in TASK_CONFIG["tasks"]:
    TASK_MODELS.append(_task["module"].split(".")[1])

SINGLE_FILE_PATH = ""
try:
    opts, args = getopt.getopt(sys.argv[1:], "hf:t:p:", ["file=","type=","path="])
except getopt.GetoptError:
    print("当前指定文件进行代码规范审查，请使用以下命令")
    print(f"Error:{sys.argv[0]} -f <filename>")
    print(f"or:{sys.argv[0]} --file <filename>")
    print(f"Error:{sys.argv[0]} -f <filename> -p <file_path> -t <model_type>")
    print(f"or:{sys.argv[0]} --file <filename> --path <file_path> --type <model_type>")
    sys, exit(0)

for opt, arg in opts:
    if opt == "-h":
        print("如需指定文件进行代码规范审查，请使用以下快捷命令")
        print(f"{sys.argv[0]} -f <filename>")
        print(f"or:{sys.argv[0]} --file <filename>")
        print("并输入模型类型：流式数据模型：flow，定时任务模型：task，其他通用模型：other。")
        print(f"Error:{sys.argv[0]} -f <filename> -p <file_path> -t <model_type>")
        print(f"or:{sys.argv[0]} --file <filename> --path <file_path> --type <model_type>")
        print("如需对项目所有py文件进行代码规范审查，请使用以下快捷命令")
        print(f"{sys.argv[0]} -f all")
        
        sys.exit()
    elif opt in ("-f", "--file"):
        if arg == "all":
            print("进入对所有项目运行py文件进行代码规范审查流程")
            SCRIPT_METHOD = "Y"
        else:
            SCRIPT_METHOD = "N"
            SINGLE_FILE_NAME_WITH_PATH = arg
    elif opt in ("-t","--type"):
        _error_count = 0
        while arg not in ModelType._member_names_:
            _error_count += 1
            if _error_count > 3:
                print("你输入了太多次错误,程序退出,如有需要请重新执行")
                sys.exit(2)
            print("模型类型输入错误，模型类型选择：流式数据模型：flow，定时任务模型：task，其他通用模型：other。")
            arg = input(f"模型类型{arg}不存在,请重新输入(已出错{_error_count},3次后自动退出):")
        SINGLE_FILE_METHOD = ModelType[arg]
    elif opt in ("-p","--path"):
        # TODO 输错后进行判断以及3次错误跳出的操作
        SINGLE_FILE_PATH = arg


if SINGLE_FILE_NAME_WITH_PATH != None and ".py" in SINGLE_FILE_NAME_WITH_PATH:
    SINGLE_FILE_NAME_WITH_PATH = SINGLE_FILE_NAME_WITH_PATH.split(".py")[0]

if SCRIPT_METHOD == "N":
    _error_count = 0
    while os.path.isfile(os.path.join(dir_path, f"{SINGLE_FILE_NAME_WITH_PATH}.py")) == False:
        _error_count += 1
        if _error_count > 3:
            print("你输入了太多次错误,程序退出,如有需要请重新执行")
            sys.exit(2)
        SINGLE_FILE_NAME_WITH_PATH = input(f"模型{SINGLE_FILE_NAME_WITH_PATH}不存在,请重新输入(已出错{_error_count},3次后自动退出):")
    _error_count = 0
    while SINGLE_FILE_METHOD not in ModelType:
        _error_count += 1
        if _error_count > 3:
            print("你输入了太多次错误,程序退出,如有需要请重新执行")
            sys.exit(2)
        print("模型类型输入错误，模型类型选择：流式数据模型：flow，定时任务模型：task，其他通用模型：other。")
        arg = input(f"模型类型{arg}不存在,请重新输入(已出错{_error_count},3次后自动退出):")
        SINGLE_FILE_METHOD = ModelType["other"]
elif SCRIPT_METHOD == None:
    SCRIPT_METHOD = input("请选择是否对项目所有运行py文件进行代码规范审查(输入Y/N):") or "Y"

_error_count = 0
while SCRIPT_METHOD.upper() not in ["Y","N"]:
    _error_count += 1
    SCRIPT_METHOD = input("请输入Y or N")
    sys.exit(2)


if SCRIPT_METHOD.upper() == "Y":
    py_files = {}
    for _root,_dirs,_files in os.walk("./"):
        for _file in _files:
            if _file.split(".")[1] == "py":
                if _root == "code_review" or _file.split(".")[0] == "code_review":
                    pass
                else:
                    py_files[f"{_file}"] = _root
    # 定时任务流式数据 暂时读取文件查询必要的函数以及备注
    # 对调用函数，进行严格审查。
    # 读取config 判断是否是数孪类流式数据模型，
    for _package, _path in py_files.items():
        _path =_path.split("./")[1]
        print(_package)
        if _path == "":
            _model =_package.split(".py")[0]
            if _model in FLOW_MODELS:
                model_check_process(_model,logging_file_path,ModelType["flow"],flow_model_list=FLOW_MODELS,task_model_list=TASK_MODELS)
            elif _model in TASK_MODELS:
                model_check_process(_model,logging_file_path,ModelType["task"],flow_model_list=FLOW_MODELS,task_model_list=TASK_MODELS)
            else:
                model_check_process(_model,logging_file_path,ModelType["task"],flow_model_list=FLOW_MODELS,task_model_list=TASK_MODELS)
        else:
            _model =_package.split(".py")[0]
            model_check_process(_model,logging_file_path,ModelType["other"],flow_model_list=FLOW_MODELS,task_model_list=TASK_MODELS,path=_path)
elif SCRIPT_METHOD.upper() == "N":
    print("单文件代码规范审查starting")
    print(SINGLE_FILE_METHOD)
    model_check_process(SINGLE_FILE_NAME_WITH_PATH,logging_file_path,SINGLE_FILE_METHOD,flow_model_list=FLOW_MODELS,task_model_list=TASK_MODELS,path=SINGLE_FILE_PATH)