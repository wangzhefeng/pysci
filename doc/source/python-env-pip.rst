
Python pip
==============

pip - The Python Package Installer

pip is the package install for Python. You can use pip to install packages from the Python Package Index(PyPI) and other indexs.

    - package installer

        - https://packaging.python.org/guides/tool-recommendations/
    
    - Python Package Index(PyPI)

        - https://pypi.org/

1.安装 pip
-----------------------------------

1.1 Install with ``get-pip.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 下载 ``get-pip.py``


    - 方法一：直接从下面的连接下载

        - `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ 

    - 方法二：使用 ``curl``

        .. code-block:: shell

            $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

2. 安装 ``pip``

    .. code-block:: shell

        $ python get-pip.py

    .. note:: 

        - ``get-pip.py`` 除了会安装 ``pip``，还会安装：

            - ``setuptools``

            - ``wheel``

3. ``get-pip.py`` 选项

    - ``--no-setuptools``

        - 不安装 ``setuptools``

    - ``--no-wheel``

        - 不安装 ``wheel``

    - pip 安装选项

        .. code-block:: shell
        
            $ python get-pip.py --no-index --find-links=/local/copies

            $ python get-pip.py --User

            $ python get-pip.py --proxy="http://[user:password@]proxy.server:port"

            $ python get-pip.py pip=9.0.2 wheel=0.30.0 setuptools=28.8.0



1.2 使用 Linux Package Managers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Installing pip/setuptools/wheel with Linux Package Managers <https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers>`_  in the `Python Packaging User Guide <https://packaging.python.org/guides/tool-recommendations/>`_ .

1.3 更新 pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Linux / macOS

    .. code-block:: shell

        $ pip install -U pip

- Windows

    .. code-block:: shell

        C:/> python -m pip install -U pip

2.安装 package
---------------------------------

2.1 Install a package from PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip install SomePackage

2.2 Install a package from PyPI or somewhere downloaded ``.whl`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip install SomePackage-1.0-py2.py3-none-any.whl

2.3 Show what files were installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip show --files SomePackage

2.4 List what package are outdated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip list --outdated


2.5 Upgrade a package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip install --upgrade SomePackage

2.6 Uninstall a package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: shell

        $ pip uninstall SomePackage


3.User Guide
------------------------------

3.1 更改 PyPi pip 源
~~~~~~~~~~~~~~~~~~~~~~

   将 pipy 的 pip 源更改为国内 pip 源

3.1.1 国内 pip 源列表
^^^^^^^^^^^^^^^^^^^^^^^^

    -  阿里云【较快】

        - `Simple Index <http://mirrors.aliyun.com/pypi/simple>`__

    -  清华大学

        - `Simple Index <https://pypi.tuna.tsinghua.edu.cn/simple/>`__

    -  中国科学技术大学

        - `Simple Index <https://pypi.mirrors.ustc.edu.cn/simple/>`__

    -  豆瓣【较快】

        - `Simple Index <http://pypi.douban.com/simple/>`__

3.1.2 临时更改 PyPi pip 源
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code:: shell

        $ pip3 install *** -i http://mirrors.aliyun.com/pypi/simple/
        $ pip3 install *** -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

3.1.3 永久更改 PyPi pip 源
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code:: shell

        $ cd ~
        $ mkdir .pip
        $ cd .pip
        $ vim pip.conf

        # [global]
        # index-url = http://mirrors.aliyun.com/pypi/simple/
        # [install]
        # trusted-host = mirrors.aliyun.com

4.Reference Guide
------------------------------

    - `pip reference guide list <https://pip.pypa.io/en/stable/reference/>`_ 