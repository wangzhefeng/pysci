
Python Env
===============================

1.Python 环境使用需求
-------------------------------

1.1 检查机器已配置的 Python 环境
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - 检查项

      - Python
      - pip

   - 检查方法

      .. code-block:: shell

         $ python --version
         $ python3 --version
         $ pip3 --version

1.2 检查机器 Python 安装的位置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - 检查项
   
      - Python
      - pip

   - 检查方法

      .. code-block:: shell
         
         $ which python
         $ which python3

         $ which pip
         $ which pip3


2.安装、卸载 Python3 环境
------------------------------

2.1 macOS
~~~~~~~~~~~~~~~~~~~~~~~~~

2.1.1 macOS version
^^^^^^^^^^^^^^^^^^^^^^^^^^

   - macOS 10.12.6(Sierra) or later(64位, no GPU support)

2.1.2 Python.org 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

# TODO

2.1.3 Brew 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

   - 安装 brew:

      .. code-block:: shell

         $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
         $ vim ~/.zshrc
         $ export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
         $ vim ~/.profile
         $ export PATH="/usr/local/opt/python/libexec/bin:$PATH"
         $ brew update

   - 安装 Python 3:

      .. code-block:: shell

         $ brew install python

   - 安装 pip3

      .. code-block:: shell

         $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
         $ python get-pip.py

2.1.4 Anaconda 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

# TODO

2.1.5 Minconda 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. Installing on macOS

      - 1.Download the installer:

         - `Miniconda - Conda documentation <https://docs.conda.io/en/latest/miniconda.html>`__

      - 2.Verify installer hashes:

         - `Downloading conda - conda 4.8.3.post5+125413ca documentation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification>`__

         .. code-block:: shell
         
            $ shasum -a 256 filename

      - 3.Install:

         .. code-block:: shell
         
            $ bash Miniconda3-lastest-MacOSX-x86_64.sh         

      - 4.Follow the prompts on the installer screens.

         - If you are unsure about any setting, accept the defaults. You can change them later.

      - 5.To make the changes take effect, close and then re-open your terminal window.
      - 6.Test your installation. In your terminal window or Anaconda Prompt, run the command ``conda list``.

         - A list of installed packages appears if it has been installed correctly.

   2. Updating Miniconda on macOS

      - 1.Open a terminal window.
      - 2.Navigate to the ``miniconda`` directory.
      - 3.Run ``conda update conda``.

   3. Uninstall Miniconda on macOS

      - 1.Open a terminal window.
      - 2.Remove the entire Miniconda install directory with:

         .. code-block:: shell
            
            $ rm -rf ~/miniconda

      - 3.OPTIONAL: Edit ``~/.bash_profile`` to remove the Miniconda directory from your PATH environment variable.
      - 4.Remove the following hidden file and folders that may have been created in the home directory:

         -  ``.condarc`` file
         -  ``.conda`` directory
         -  ``.continuum`` directory
         - By running:

            .. code-block:: shell
            
               $ rm -rf ~/.condarc ~/.conda ~/.continuum

2.1.6 pyenv 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - 参考 pyenv 的使用


2.2 Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.2.1 Linux Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   -  Ubuntu 16.04 LTS
   -  Ubuntu 18.04 LTS
   -  Ubuntu 20.04 LTS

2.2.2 安装 Python 3.7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - 配置Ubuntu环境：

   .. code-block:: shell

      # software-properties-common
      $ sudo apt-get install software-properties-common
      # This PPA contains more recent Python versions packaged for Ubuntu
      # https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
      $ sudo add-apt-repository ppa:deadsnakes/ppa
      # 更新软件源
      $ sudo apt-get update

   - Python 3.7 及包管理工具：

   .. code-block:: shell

      # python3.7
      $ sudo apt-get install python3.7

      # pip3
      $ sudo apt-get install python3-pip
      $ sudo apt-get install python3.7-dev
      $ sudo apt-get install python-dev
      $ sudo apt-get install python3.7-gdbm

      # 安装验证
      $ python3.7 --version

2.2.3 安装完成后，修改 python3 的默认指向
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: shell

      # 删除软连接
      $ sudo rm /usr/bin/python3
      $ sudo rm /usr/bin/python

      # 创建软连接
      $ sudo ln -s python3.7 /usr/bin/python3
      $ sudo ln -s python3.7 /usr/bin/python

      # 修改验证
      $ which python3     # 软连接路径
      $ python3 --version

      $ which pip3        # 软连接路径
      $ pip3 --version

   - 若更换python版本后出现 ``No module named "apt_pkg"``\ ：

   .. code-block:: shell

      $ sudo apt-get remove --purge python-apt
      $ sudo apt-get install python-apt -f
      $ sudo find / -name "apt_pkg.cpython-36m-x86_64-linux-gnu.so"
      $ cd /usr/lib/python3/dist-packages/
      $ sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.cpython-37m-x86_64-linux-gnu.so

2.2.4 卸载 Python 3.7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: shell

      # 卸载 Python 3.7
      $ sudo apt-get remove python3.7

      # 卸载 Python 3.7 及其依赖
      $ sudo apt-get remove --auto-remove python3.7

      # 清除 Python 3.7
      $ sudo apt-get purge python3.7
      $ sudo apt-get purge [--auto-remove] python3.7

2.3 Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
2.3.1 管网下载安装、手动配置环境变量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - https://www.python.org/downloads/windows/

.. note:: 
   
   注意：

    - 升级系统 pip 可能会导致问题。如果不是在虚拟环境中，
      请针对下面的命令使用 ``python3 -m pip``。
      这样可以确保您升级并使用 Python pip，而不是系统 pip。

2.3.2 Chocolatey 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 环境

   - Windows 7+ / Windows Server 2003+
   - PowerShell v2+ (minimum is v3 for install from this website due to TLS 1.2 requirement)
   - .NET Framework 4+ (the installation will attempt to install .NET 4.0 
     if you do not have it installed)(minimum is 4.5 for install from this 
     website due to TLS 1.2 requirement)

2. 安装 Chocolatey

   - `Installing Chocolatey <https://chocolatey.org/install#individual>`_ 

3. 安装 Python 3

   .. code-block:: shell
   
      C:/> choco install python



3.创建 Python 虚拟环境
--------------------------

3.1 virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~



   - Ubuntu/macOS

      .. code-block:: shell

         $ pip install virtualenv
         $ mkdir myproject
         $ cd myproject
         $ virtualenv -system-site-packages -p python3 ./venv
         # $ virtualenv -no-site-packages -p python3 ./venv
         $ source ./venv/bin/activate
         $ (venv) $ pip install --upgrade pip
         $ (venv) $ pip list
         $ (venv) $ deactivate

   - Windows

      .. code-block:: shell

         C:\> virtualenv --system-site-packages -p python3 ./venv
         
         (venv) C:\> .\venv\Scripts\activate
         (venv) C:\> pip install --upgrade pip
         (venv) C:\> pip list
         (venv) C:\> deactivate

3.2 virtualenvwrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~

3.2.1 Install packages
^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      # pipx install virtualenv
      # $ pipx install virtualenv

      # $ pip3 install virtualenv
      # $ sudo pip3 install virtualenv
      $ sudo apt-get install virtualenv

      # $ sudo pip3 install virtualenvwrapper
      $ sudo apt-get install virtualenvwrapper

3.2.2 Configuration 
^^^^^^^^^^^^^^^^^^^^^^^^^^

Location of Environments and Project Directories

   .. code:: shell

      export WORKON_HOME=~/Envs
      mkdir -p $WORKON_HOME
      # source /Users/zfwang/opt/anaconda3/bin/virtualenvwrapper.sh

``~/.zshrc`` 配置：

   .. code:: shell

      # ~/.zshrc
      export WORKON_HOME=~/Envs
      export PATH=$PATH:$WORKON_HOME
      source /Users/zfwang/opt/anaconda3/bin/virtualenvwrapper.sh

      # macOS
      export WORKON_HOME=~/.virtualenv
      export PATH=$PATH:$WORKON_HOME
      export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
      export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
      export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
      # export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
      source /usr/local/bin/virtualenvwrapper.sh

3.2.3 Create Virtual Env
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 快速开始

   .. code:: shell

      # List the virtual env
      $ workon

   .. code:: shell

      # make a virtual env
      $ mkvirtualenv env1
      $ mkvirtualenv --system-site-packages env1

      # install packages
      (env1)$ pip3 install django

      # see the new package installed
      (env1)$ lssitepackages

      # see all virtual envs
      (env1)$ ls $WORKON_HOME

   .. code:: shell

      # switch between environments
      (env1)$ mkvirtualenv env2
      (env2)$ ls $WORKON_HOME

   .. code:: shell

      (env2)$ workon env1
      (env1)$ echo $VIRTUAL_ENV

      # `psotmkvirtualenv`
      (env1)$ echo 'cd $VIRTUAL_ENV' >> $WORKON_HOME/postactivate

      (env1)$ workon env2
      (env2)$ echo 'pip3 install numpy' >> $WORKON_HOME/postactivate
      (env2)$ mkvirtualenv env3

2. Command Reference

   -  Managing Env
   
      -  ``mkvirtualenv``
      -  ``mktmpenv``
      -  ``lsvirtualenv``
      -  ``showvirtualenv``
      -  ``rmvirtualenv``
      -  ``cpvirtualenv``
      -  ``allvirtualenv``
   
   -  Controlling Active Env
   
      -  ``workon``
      -  ``deactivate``
   
   -  Navigating to an Env
   
      -  ``cdvirtualenv``
      -  ``cdsitepackages``
      -  ``lssitepackages``
   
   -  Path Management
   
      -  ``add2virtualenv``
      -  ``toggleglobalsitepackages``
   
   -  Project Directory Management
   
      -  ``mkproject``
      -  ``setvirtualenvproject``
      -  ``cdproject``
   
   -  Managing Installed Packages
   
      -  ``wipeenv``
   
   -  Others
   
      -  ``virtualenvwrapper``

3.3 pipx
~~~~~~~~~~~~~~~~~~~~~~~~~~

3.3.1 安装 pipx
^^^^^^^^^^^^^^^^^^^^^^^^^^






3.4 pipenv
~~~~~~~~~~~~~~~~~~~~~~~~~~




   - `Pipenv <https://docs.pipenv.org/>`_ 


3.5 pyenv
~~~~~~~~~~~~~~~~~~~~~~~~~~

   1. 安装多个版本的 Python
      - 在 user 下安装 Python
      - 在 user 下安装多个版本的 Python
   2. 安装 Python 的最新开发版本
   3. 在已安装的版本之间切换
   4. 使用虚拟环境 pyenv
   5. 自动激活不同的 Python 版本和虚拟环境


.. note:: 

   这里只介绍 Linux 和 macOS 的使用，对于 Windows 用户参考 https://github.com/pyenv-win/pyenv-win

3.5.1 安装 pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 构建依赖

   在安装 pyenv 之前，需要安装一些操作系统特定的依赖项，这些依赖项主要是用 C 编写的开发应用程序，
   并且是必需的，因为 pyenv 是通过从源码构建来安装 Python 的

   - Ubuntu/Debian
   
      .. code-block:: shell
   
         $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
           libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
           libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
   
   - Fedora/CentOS/RHEL
   
      .. code-block:: shell
      
         $ sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite \
           sqlite-devel openssl-devel xz xz-devel libffi-devel

   - Alpine

      .. code-block:: shell
      
         $ apk add libffi-dev ncurses-dev openssl-dev readline-dev \
           tk-dev xz-dev zlib-dev
   

   - openSUSE

      .. code-block:: shell
      
         $ zypper in zlib-devel bzip2 libbz2-devel libffi-devel \
           libopenssl-devel readline-devel sqlite3 sqlite3-devel xz xz-devel

   - macOS
   
      .. code-block:: shell
         
         $ brew install openssl readline sqlite3 xz zlib
         $ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

2. 安装 pyenv(使用 pyenv-installer 项目)，安装内容:

   - 1.pyenv: pyenv 应用
   - 2.pyenv-virtualenv: pyenv 和虚拟环境的插件
   - 3.pyenv-update: pyenv 的更新插件
   - 4.pyenv-doctor: pyenv 及其构建依赖的验证插件
   - 5.pyenv-which-ext: 自动查找系统命令的插件

   .. code-block:: shell
      
      $ curl https://pyenv.run | bash

      WARNING: seems you still have not added 'pyenv' to the load path.

      Load pyenv automatically by adding
      the following to ~/.bashrc or /.zshrc:

      export PATH="$HOME/.pyenv/bin:$PATH"
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"

3.5.2 安装、卸载 Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 查看使用 pyenv 可以安装的 Python 版本

   - 查看所有可用的 Cython 3.6~3.8

      .. code-block:: shell
      
         $ pyenv install --list | grep " 3\.[6,7.8]"

   - 查看所有可用的 Jython 版本

      .. code-block:: shell
      
         $ pyenv install --list | grep "jython"
         $ pyenv install --list

2. 确定要安装的 Python 版本后，安装 Python

      .. code-block:: shell
      
         $ pyenv install -v 3.7.10

3. 查看 Python 安装位置

   pyenv 安装的每个 Python 版本都位于 pyenv 的根目录中

   .. code-block:: shell
   
      $ ls ~/.pyenv/version/
      3.7.10
      $ which python
      /Users/zfwang/.pyenv/shims/python
      $ which python3
      /Users/zfwang/.pyenv/shims/python3
      $ pyenv which python
      /Users/zfwang/.pyenv/versions/3.7.10/bin/python
      $ pyenv which python3
      /Users/zfwang/.pyenv/versions/3.7.10/bin/python3

4. 删除某个 Python 版本

   .. code-block:: shell
   
      $ rm -rf ~/.pyenv/version/3.7.10
      # or 卸载
      $ pyenv uninstall 3.7.10

3.5.3 切换 Python 版本
^^^^^^^^^^^^^^^^^^^^^^^^^^

- pyenv 如何准确地解析使用的 Python 版本

   .. image:: ../images/pyenv-pyramid.png
   
   .. code-block:: shell
   
      # 查看当前已经下载的、使用的 Python 版本
      $ pyenv versions

      # 设置全局 Python 版本
      $ pyenv global 2.7.15
      $ pyenv versions
      $ cat ~/.pyenv/version

      # 创建一个 .python-version 文件
      $ pyenv local 3.7.10
      $ pyenv versions
      $ ls -a
      $ cat .python-version

      # 设置 shell 的 Python 版本
      $ pyenv shell 3.8-dev
      $ pyenv version
      $ echo $PYENV_VERSION

3.5.4 构建 Python 虚拟环境
^^^^^^^^^^^^^^^^^^^^^^^^^^

   pyenv 、pyenv-virtualenv 与 virtualenv、venv 的区别

      - pyenv 管理 Python 的多个版本
      - virtualenv/venv 管理特定版本 Python 的虚拟环境
      - pyenv-virtualenv 管理不同版本 Python 的虚拟环境

1. 创建虚拟环境

   .. code-block:: shell
   
      $ pyenv virtualenv <python_version> <envirionment_name>

2. 激活虚拟环境

   .. code-block:: shell
   
      $ pyenv local <envirionment_name
      $ pyenv which python
      $ pyenv which pip
      # or
      $ pyenv activate <envirionment_name>
      $ pyenv deactivate


3.5.5 使用多个 Python 环境
^^^^^^^^^^^^^^^^^^^^^^^^^^

   假设在机器中安装了如下 Python 版本：

      - 2.7.15
      - 3.6.8
      - 3.8-dev

   现在想要处理两个项目：

      1. project1 支持 python2.7 和 Python3.6
      2. project2 支持 python3.6 和 Python3.8-dev 的测试

1. 首先为 project1 创建一个虚拟环境

   .. code-block:: shell
   
      $ cd project1/
      $ pyenv which python
      $ pyenv virtualenv 3.6.8 project1
      $ pyenv local project1
      $ python -V

2. 为 project2 创建一个虚拟环境

   .. code-block:: shell
   
      $ cd project2/
      $ pyenv which python
      $ pyenv virtualenv 3.8-dev project2
      $ pyenv local project2
      $ python -V

3. 同时激活多个版本

   假设 project2 使用 3.8 中的实验性功能，但仍然想让代码适用于 Pyton3.6 

   .. code-block:: shell
      
      $ pyenv local project2 3.6.8
      $ python3.6 -V

3.5.6 探索 pyenv 命令
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. 查看 pyenv 所有可用的命令完整列表

   .. code-block:: shell
   
      $ pyenv commands
      $ pyenv <pyenv_commands> --help

2. ``install``

   .. code-block:: shell
   
      # 安装 python 特定版本
      $ pyenv install 3.6.8
      # 列出所有可供安装的 Python 版本
      $ pyenv install -l/--list
      # 构建调试版本的 Python
      $ pyenv install -g/--debug
      # 详细模式: 将编译状态打印到标准输出
      $ pyenv install -v/--verbose

3. ``versions`` 

   .. code-block:: shell

      # 显示所有当前安装的 Python 版本,包括虚拟环境
      $ pyenv versions

4. ``which``

   .. code-block:: shell
   
      # 确定系统可执行文件的完整路径
      $ pyenv which python
      $ pyenv which pip

5. ``global``

   .. code-block:: shell
      
      $ pyenv global 3.7.10

6. ``local``

   .. code-block:: shell
   
      # 设置特定与应用程序的 Python 版本
      # 此命令会在当前目录中创建一个 .python-version 文件，进入该目录会自动激活该文件中的 Python 版本
      $ pyenv local 3.6

7. ``shell``

   .. code-block:: shell
   
      # 设置特定于 shell 的 Python 版本
      $ pyenv shell 3.8-dev


3.6 Conda
~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: shell

      $ conda create -n venv pip python3.7
      $ source activate venv
      (venv) $ pip install --ignore-installed --upgrade packageURL
      (venv) $ source deactivate

3.7 virtualenv-burrito
~~~~~~~~~~~~~~~~~~~~~~~~~~

3.8 autoenv
~~~~~~~~~~~~~~~~~~~~~~~~~~


4.Python 项目管理
------------------------------

4.1 ``requirements.txt``
~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Method 1:

      .. code:: shell

         # 生成 requirements.txt
         pip freeze --local > requirements.txt

         # 安装 requirements.txt
         pip install -r requirements.txt


   - Method 2:

      .. code:: shell

         pip install pipreqs

      .. code:: python

         pipreqs ./ encoding=utf-8

4.2 README.md
~~~~~~~~~~~~~~~~~~~~~~~~~~


4.3 Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~


4.4 Doc
~~~~~~~~~~~~~~~~~~~~~~~~~~



4.5 unittest
~~~~~~~~~~~~~~~~~~~~~~~~~~


4.6 setup.py
~~~~~~~~~~~~~~~~~~~~~~~~~~


1.检查已配置的 Python 环境
------------------------------

   - 检查项

      - Python

      - pip

      - conda

      - virtualenv

      - virtualenvwrapper

   - 检查方法

      .. code-block:: shell

         $ python3 --version
         $ pip3 --version
         $ conda --version
         $ virtualenv --version
         $ virtualenvwrapper --version

2.安装 Python 环境
------------------------------

2.1 macOS Python 3 Env
~~~~~~~~~~~~~~~~~~~~~~~~~

2.1.1 macOS version
^^^^^^^^^^^^^^^^^^^^^^^^^^

   - macOS 10.12.6(Sierra) or later(64位, no GPU support)

2.1.2 Python.org 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      $ test


2.1.3 Brew 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

   - 安装 brew:

      .. code-block:: shell

         $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
         $ export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
         $ brew update

   - 安装 Python 3:

      .. code-block:: shell

         $ brew install python

   - 安装 pip3

      .. code-block:: shell

         $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
         $ python get-pip.py

   - 安装 virtualenv, virtualenvwrapper

      .. code-block:: shell

         $ sudo pip3 install -U virtualenv         # system-wide install
         $ sudo pip3 install -U virtualenvwrapper # system-wide install


2.1.4 Anaconda/Minconda 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   1. Installing on macOS

      - (1)Download the installer:

         - `Miniconda - Conda documentation <https://docs.conda.io/en/latest/miniconda.html>`__

      - (2)Verify installer hashes:

         - `Downloading conda - conda 4.8.3.post5+125413ca documentation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification>`__

         .. code:: shell

            shasum -a 256 filename

      - (3)Install:

         .. code:: shell

            bash Miniconda3-lastest-MacOSX-x86_64.sh

      - (4)Follow the prompts on the installer screens.

         - If you are unsure about any setting, accept the defaults. You can change them later.

      - (5)To make the changes take effect, close and then re-open your terminal window.

      - (6)Test your installation. In your terminal window or Anaconda Prompt, run the command ``conda list``.

         - A list of installed packages appears if it has been installed correctly.


   2. Updating Miniconda on macOS

      - (1)Open a terminal window.

      - (2)Navigate to the ``miniconda``\ directory.

      - (3)Run ``conda update conda``.


   3. Uninstall Miniconda on macOS

      - (1)Open a terminal window.

      - (2)Remove the entire Miniconda install directory with:

         .. code:: shell

            rm -rf ~/miniconda

      - (3)OPTIONAL: Edit ``~/.bash_profile`` to remove the Miniconda directory from your PATH environment variable.

      - (4)Remove the following hidden file and folders that may have been created in the home directory:

         -  ``.condarc`` file

         -  ``.conda`` directory

         -  ``.continuum`` directory

         - By running:

            .. code:: shell

               rm -rf ~/.condarc ~/.conda ~/.continuum



2.2 Ubuntu Python 3 Env
~~~~~~~~~~~~~~~~~~~~~~~~~

2.2.1 Linux Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   -  Ubuntu 16.04 LTS

   -  Ubuntu 18.04 LTS

   -  Ubuntu 20.04 LTS

2.2.2 安装 Python 3.7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 配置Ubuntu环境:

   .. code:: shell

      # 更新系统软件源
      sudo apt-get update

      # software-properties-common
      sudo apt-get install software-properties-common

      # This PPA contains more recent Python versions packaged for Ubuntu.
      sudo add-apt-repository ppa:deadsnakes/ppa
      # sudo add-apt-repository ppa:jonathonf/pyhton3.6

      # 更新软件源
      sudo apt-get update

- Python 3.7 及包管理工具:

   .. code:: shell

      # python3.7
      sudo apt-get install python3.7

      # pip3
      sudo apt-get install python3-pip
      sudo apt-get install python3.7-dev
      sudo apt-get install python-dev
      sudo apt-get install python3.7-gdbm

      # 安装验证
      python3.7 --version


2.2.3 修改 python3 的默认指向
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      # 删除软连接
      sudo rm /usr/bin/python3
      sudo rm /usr/bin/python

      # 创建软连接
      sudo ln -s python3.7 /usr/bin/python3
      sudo ln -s python3.7 /usr/bin/python

      # 修改验证
      which python3 # 软连接路径
      python3 --version

      which pip3    # 软连接路径
      pip3 --version

   - 若更换python版本后出现 ``No module named "apt_pkg"``\ :

      .. code:: shell

         sudo apt-get remove --purge python-apt
         sudo apt-get install python-apt -f
         sudo find / -name "apt_pkg.cpython-36m-x86_64-linux-gnu.so"
         cd /usr/lib/python3/dist-packages/
         sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.cpython-37m-x86_64-linux-gnu.so


2.2.4 安装虚拟环境
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      pip3 install virtualenv
      pip3 install virtualenvwrapper

      sudo install virtualenv
      sudo install virtualenvwrapper


2.2.5 卸载 Python3.7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      # 卸载Python3.7
      sudo apt-get remove python3.7

      # 卸载 Python3.7 及其依赖
      sudo apt-get remove --auto-remove python3.7

      # 清除 Python3.7
      sudo apt-get purge python3.7
      sudo apt-get purge [--auto-remove] python3.7


   .. code-block:: shell
      
      $ sudo apt update

      # 安装 Python 3
      $ sudo apt install python3-dev

      # 安装 pip3
      $ sudo apt install python3-pip
      
      # 安装 virtualenv, virtualenvwrapper
      $ sudo pip3 install -U virtualenv
      $ sudo pip3 install -U virtualenvwrapper


2.3 Windows Python 3 Env
~~~~~~~~~~~~~~~~~~~~~~~~~
 
   - https://www.python.org/downloads/windows/

   .. code-block:: shell
      
      # 安装 virtualenv, virtualenvwrapper
      C:\> pip3 install -U pip virtualenv
      C:\> pip3 install -U pip virtualenvwrapper


.. note:: 注意:

    升级系统 pip 可能会导致问题。如果不是在虚拟环境中，
    请针对下面的命令使用 ``python3 -m pip``。
    这样可以确保您升级并使用 Python pip，而不是系统 pip。





3.创建 Python 虚拟环境
--------------------------

3.1 Ubuntu/macOS
~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: shell

      $ virtualenv -system-site-packages -p python3 ./venv
      $ source ./venv/bin/activate
      $ (venv) $ pip install --upgrade pip
      $ (venv) $ pip list
      $ (venv) $ deactivate

3.2 Windows
~~~~~~~~~~~~~~~~~~~

   .. code-block:: shell

      C:\> virtualenv --system-site-packages -p python3 ./venv
      
      (venv) C:\> .\venv\Scripts\activate
      (venv) C:\> pip install --upgrade pip
      (venv) C:\> pip list
      (venv) C:\> deactivate


3.3 Conda
~~~~~~~~~~~~~~~~~~

   .. code-block:: shell

      $ conda create -n venv pip python3.7
      $ source activate venv
      (venv) $ pip install --ignore-installed --upgrade packageURL
      (venv) $ source deactivate


