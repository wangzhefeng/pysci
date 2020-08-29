
Python Env
========================

1.检查已配置的 Python 环境
------------------------------

   - 检查项

      - Python

      - pip

      - virtualenv

      - virtualenvwrapper

   - 检查方法

      .. code-block:: shell

         $ python3 --version
         $ pip3 --version
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

         $ sudo pip3 install -U virtualenv        # system-wide install
         $ sudo pip3 install -U virtualenvwrapper # system-wide install



2.1.4 Anaconda 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      $ test


2.1.5 Minconda 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Installing on macOS

   - 1.Download the installer:

      - `Miniconda - Conda documentation <https://docs.conda.io/en/latest/miniconda.html>`__

   - 2.Verify installer hashes:

      - `Downloading conda - conda 4.8.3.post5+125413ca documentation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification>`__

      .. code:: shell

         shasum -a 256 filename

   - 3.Install:

      .. code:: shell

         bash Miniconda3-lastest-MacOSX-x86_64.sh

   - 4.Follow the prompts on the installer screens.

      - If you are unsure about any setting, accept the defaults. You can change them later.

   - 5.To make the changes take effect, close and then re-open your terminal window.

   - 6.Test your installation. In your terminal window or Anaconda Prompt, run the command ``conda list``.

      - A list of installed packages appears if it has been installed correctly.


- Updating Miniconda on macOS

   - 1.Open a terminal window.

   - 2.Navigate to the ``miniconda``\ directory.

   - 3.Run ``conda update conda``.


- Uninstall Miniconda on macOS

   - 1.Open a terminal window.

   - 2.Remove the entire Miniconda install directory with:

      .. code:: shell

         rm -rf ~/miniconda

   - 3.OPTIONAL: Edit ``~/.bash_profile`` to remove the Miniconda directory from your PATH environment variable.

   - 4.Remove the following hidden file and folders that may have been created in the home directory:

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

- 配置Ubuntu环境：

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

- Python 3.7 及包管理工具：

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


2.2.3 安装完成后，修改python3的默认指向
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

   - 若更换python版本后出现 ``No module named "apt_pkg"``\ ：

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


.. note:: 注意：

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


.. _header-n26:

2.1 ``pipx``
~~~~~~~~~~~~

.. code:: shell

   brew install pipx


.. _header-n28:

2.2 使用 ``virtualenv`` 创建 Python 虚拟环境
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   -  ``virtualenv`` 是如何创建“独立”的 Python
      运行环境的呢？原理很简单，就是把系统 Python 复制一份到
      ``virtualenv`` 的环境，用命令 ``source venv/bin/activate``
      进入一个 ``virtualenv`` 环境时，\ ``virtualenv``
      会修改相关环境变量，让命令 ``python`` 和 ``pip`` 均指向当前的
      ``virtualenv`` 环境

   -  ``virtualenv`` 为应用提供了隔离的 Python
      运行环境，解决了不同应用间多版本的冲突问题

1. 安装 ``virtualenv``

.. code:: shell

   $ pip3 install virtualenv

1. 为项目创建一个独立的 Python 运行环境

第一步，创建项目目录：

.. code:: shell

   $ mkdir myproject
   $ cd myproject

第二步，创建一个独立的 Python 运行环境，命名为 ``venv``\ ：

   命令 ``virtualenv`` 就可以创建一个独立的 Python
   运行环境，还加上了参数 ``--no-site-packages``\ ，这样，已经安装到系统
   Python
   环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的
   Python 运行环境

.. code:: shell

   $ virtualenv -p /Users/zfwang/opt/anaconda3/bin/python3 --no-site-packages venv

第三步，进入 ``venv`` 运行环境

   在 ``venv`` 环境下，用 ``pip`` 安装的包都被安装到 ``venv``
   这个环境下，系统 Python 环境不受任何影响。也就是说，\ ``venv``
   环境是专门针对 ``myproject`` 这个应用创建的

.. code:: shell

   $ source venv/bin/activate

第四部，退出当前的 ``venv`` 环境

   此时就回到了正常的环境，现在 ``pip3`` 或 ``python3``
   均是在系统Python环境下执行

.. code:: shell

   $ deactivate


.. _header-n56:

2.3 使用 ``virtualwrapper`` 创建 Python 虚拟环境
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _header-n57:

2.3.1 Install packages
^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   # pipx install virtualenv
   # $ pipx install virtualenv

   # $ pip3 install virtualenv
   # $ sudo pip3 install virtualenv
   $ sudo apt-get install virtualenv

   # $ sudo pip3 install virtualenvwrapper
   $ sudo apt-get install virtualenvwrapper


.. _header-n59:

2.3.2 Configuration 
^^^^^^^^^^^^^^^^^^^^

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



.. _header-n64:

2.3.3 Create Virtual Env
^^^^^^^^^^^^^^^^^^^^^^^^

1.快速开始

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

2.Command Reference

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

3.Managing Env

3.1 Create Env in ``WORKON_HOME``

.. code:: shell

   $ workon
   $ mkvirtualenv [-a project_path] [-i package] [-r requirements.txt] [virtualenv options] ENVNAME

3.2 Create Env in ``WORKON_HOME``

.. code:: shell

   $ mktmpenv [(-c|--cd)|(-n|--no-cd)] [VIRTUALENV_OPTIONS]

3.3 List all of the Env

.. code:: shell

   $ lsvirtualenv [-b] [-l] [-h]

3.4 Show the Details for a single Env

.. code:: shell

   $ showvirtualenv [env]

3.5 Remove an Env from ``WORKON_HOME``

.. code:: shell

   $rmvirtualenv ENVNAME

3.6 Duplicate an existing Env

.. code:: shell

   $ cpvirtualenv ENVNAME [TARGETENVNAME]

3.7 Run a command in all ENV under ``WORKON_HOME``

.. code:: shell

   $ allvirtualenv command with arguments

.. code:: shell

   $ allvirtualenv pip install -U pip

4.Controlling Active Env

4.1 List or Change working Env

.. code:: shell

   $ workon [(-c|--cd)|(-n|--no-cd)] [environment_name|"."]

4.2 Deactivate

.. code:: shell

   $ deactivate

5.Navigating to an Env

5.1 Change the CWD to ``$VIRTUAL_ENV``

.. code:: shell

   cdvirtualenv [subdir]

5.2 Change the CWD to ``site-packages`` for ``$VIRTUAL_ENV``

.. code:: shell

   cdsitepackages [subdir]

5.3 Show the content of the ``site-package`` of the CAV(current-active
virtualenv)

.. code:: shell

   lssitepackages

6.Path Management

6.1 Adds the specified directories to the Python path for the
currently-active virtualenv.

.. code:: shell

   $ add2virtualenv directory1 directory2 ...

6.2 Controls whether the active virtualenv will access the packages in
the global Python site-packages directory.

.. code:: shell

   $ toggleglobalsitepackages [-q]

7.Project Directory Management

7.1 Create a Env in ``WORKON_HOME`` and Pro in ``PROJECT_HOME``

.. code:: shell

   mkproject [-f|--force] [-t template] [virtualenv_options] ENVNAME

7.2 Bind an existing Env to an existing Proj

.. code:: shell

   $ cd /home/zfwang/Documents/ml
   $ workon
   $ workon mlenv
   (mlenv)$ setvirtualenvproject [virtualenv_path project_path]
   (mlenv)$ setvirtualenvproject mlenv mlproj
   (mlenv)$ cd mlproj

7.3 Change the CWD to one specified as the ProjDir for the active
Virtual

.. code:: shell

   $ cdproject

8.Managing Installed Packages

8.1 Remove all of the installed third-party packages in the current
virtualenv

.. code:: shell

   $ wipeenv

9.Others

.. code:: shell

   $ virtualenvwrapper


.. _header-n177:

2.4 ``requirements.txt``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Method 1:

.. code:: shell

   # 生成 requirements.txt
   pip freeze --local > requirements.txt

   # 安装 requirements.txt
   pip install -r requirements.txt


Method 2:

.. code:: shell

   pip install pipreqs

.. code:: python

   pipreqs ./ encoding=utf-8
