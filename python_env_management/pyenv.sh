# ------------------------------------------------
# 创建使用需求文件 requirements.txt
# ------------------------------------------------
# 使用pip在虚拟环境中生成requirements.txt，用于记录所有依赖包及其精确地版本号，以便新环境部署
(venv)$ pip freeze >requiements.txt

# 当需要创建某个虚拟环境的完全副本时，可以创建一个新的虚拟环境，然后进入新的虚拟环境
(venv)$ pip install -r requirements.txt