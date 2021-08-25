
Python conda
==============

1.Conda 使用介绍
----------------------------

1.1 Conda 介绍
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

系统要求:

    - 32- or 64-bit computer.
    - For Miniconda---400 MB disk space.
    - For Anaconda---Minimum 3 GB disk space to download and install.
    - Windows, macOS, or Linux.

下载安装方式：

    - Miniconda

        - conda
        - conda dependencies

    - Anaconda

        - conda
        - 7500+ open-source packages

    - Silent mode

        - Windows
        - macOS
        - Linux

    - 多 Python 环境中安装

        - 为了安装 Conda 不需要卸载其他 Python 环境，其他 Python 环境如下：
            
            - 系统中自带安装的 Python
            - 从 macOS Homebrew 包管理工具中安装的 Python
            - 从 pip 安装的 Python 包

    .. note:: 

        1.如何检查当前环境中是否安装了 Conda?

            - Windows(Anaconda Prompt)

                - ``echo %PATH%``
            
            - macOS 和 Linux

                - ``echo $PAHT``

        2.如何检查当前环境中默认的 Python 环境？
            
            - Windows(Anaconda Prompt)

                - ``where python``
            
            - macOS 和 Linux

                - ``which python``

1.2 Conda 安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.Conda 下载

    - `Anaconda3 <https://www.anaconda.com/products/individual>`_ 

        - `Anaconda 老版本 <https://repo.anaconda.com/archive/>`_ 

    - `Miniconda3 <https://docs.conda.io/en/latest/miniconda.html>`_ 

        - `Miniconda 老版本 <https://repo.anaconda.com/miniconda/>`_ 

    - `Anaconda Enterprise <https://www.anaconda.com/products/enterprise>`_ 

2.Conda 安装

    - Windows
    
    - macOS

    - Linux

2.Conda 使用
----------------------------

    Package, dependency and environment management for any 
    language—Python, R, Ruby, Lua, Scala, Java, JavaScript, 
    C/ C++, FORTRAN, and more.

        - conda 管理

        - packages 管理

        - virtual packages 管理

        - environment 管理

        - channels 管理

        - Python 管理

2.1 conda 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.验证 conda 是否已经安装

    .. code-block:: shell
    
        conda --version

2.确定 conda 版本

    .. code-block:: shell
    
        conda info
        conda -V

3.将 conda 更新到当前版本

    .. code-block:: shell
    
        conda update conda

4.禁止显示有关更新 conda 的警告消息

    .. code-block:: shell
    
        conda update -n base conda
    
    .. code-block:: shell
    
        conda config --set notify_outdated_conda false
    
    .. code-block:: shell
    
        # ~/.conda
        notify_updated_conda: false


2.2 packages 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




2.2 virtual packages 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




2.2 environment 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




2.2 channels 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




2.2 Python 管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda treats Python the same as any other package, so it is easy to manage and update multiple installations.

    - Anaconda supports Python 2.7, 3.6, and 3.7. The default is Python 2.7 or 3.7, depending on which installer you used:

        - For the installers "Anaconda" and "Miniconda," the default is 2.7.

        - For the installers "Anaconda3" or "Miniconda3," the default is 3.7.

1.查看可供 conda 下载的 Python 版本列表

    .. code-block:: shell

        conda search python
        conda search --full-name python

2.安装其他版本的 Python

    .. note:: 

        安装其他版本的 Python 并不覆盖目前已经存在的版本.

    (1)创建新环境

        .. code-block:: shell
        
            conda create -n py36 python=3.6 anaconda
            conda create -n py36 python=3.7 miniconda
            conda create -n py27 python=2.7 anaconda
    
    (2)激活新环境

        - 参考 **切换其他版本的 Python**

    (3)验证新环境是否为当前环境
    (4)验证当前环境

        .. code-block:: shell

            python --version

3.切换其他版本的 Python

    - (1)如果当前环境是 conda 环境:

        1.激活环境

            .. code-block:: shell

                conda activate myenv

        2.停用环境

            .. code-block:: shell

                conda deactivate

    - (2)如果当前环境不是 conda 环境:

        - Windows 

            .. code-block:: shell
            
                D:\Miniconda\Script\acitvate base
        
        - macOS 或 Linux

            .. code-block:: shell

                ~/opt/miniconda3/bin/activate base

    - 嵌套环境

        .. code-block:: shell
            
            (doc)$ codna activate --stack myenv
            $ conda config -set auto_stack 1

    - Conda init 

        .. code-block:: shell
        
            conda init 
            auto_activate_base: bool


4.更新或升级 Python

    .. code-block:: shell

        conda update python
        conda install python=3.6

