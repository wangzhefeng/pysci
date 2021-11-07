###########################################################################
# 搭建python machine-learning项目环境
###########################################################################
# 创建项目目录
export ML_PATH="$HOME/project/mlenv"
mkdir -p $ML_PATH

# 更新Python包管理器pip
pip --version
pip install --upgrade pip

# 创建项目的虚拟环境
pip install --user --upgrade virtualenv
cd $ML_PATH
virtualenv env

# 激活虚拟环境
cd $ML_PATH
source env/bin/activate

# 安装模块及依赖项
pip install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn
python -c "import jupyter, matplotlib, numpy, pandas, scipy, sklearn"

# 启动jupyter
jupyter notebook

