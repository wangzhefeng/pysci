.. _header-n0:

Python 环境管理
===============

-  ``virtualenv``

-  ``virtualenvwrapper``

-  ``pipx``


.. _header-n10:

1. Python 项目结构(GitHub version)
----------------------------------

-  root

   -  ``scripts\``

   -  ``.gitignore``

   -  ``REAMDE.md``

   -  ``requirements.txt``

   -  ``setup.py``



.. _header-n25:

2. 创建 Python 虚拟环境
-----------------------


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
