
Python Jupyter
=======================

1.Install Jupyter
------------------------

    - 相关库

        - ``jupyter``
        - ``notebook``
        - ``jupyterlab``
        - ``ipykernel``
        - ``jupyter-client``
        - ``jupyter-console``
        - ``jupyter-core``
        - ``jupyter-server``
        - ``jupyterlab-pygments``
        - ``jupyterlab-server``
        - ``voila``

1.1 安装 Jupyter 相关库
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Jupyter

        .. code-block:: shell

            $ pip install jupyter

    - Jupyter Notebook

        .. code-block:: shell

            $ pip install notebook

    - Jupyter Lab

        .. code-block:: shell

            $ pip install jupyterlab

    - Voila

        .. code-block:: shell

            $ pip install voila

1.2 Jupyter kernel 设置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - 安装 ``ipykernel`` 在当前环境：

        .. code-block:: shell

            $ pip instll ipykernel

    - 查看 kernel

        .. code-block:: shell

            $ jupyter kernelspec list

    - 将环境加入 Jupyter Lab

        .. code-block:: shell
            
            $ workon pysci
            $ python -m ipykernel install --prefix=/Users/zfwang/.virtualenv/pysci/ --name pysci
            $ ipykernel install --name env_name --user

    - 删除 kernel

        .. code-block:: shell

            $ jupyter kernelspec remove python3

2.JupyterLab 1.0
-------------------------

    - JupyterLab 帮助

        .. code-block:: shell

            $ jupyter lab -h

    - 登录 JupyterLab

        - ``--port``
            - 指定端口号
        - ``--ip``
            - 指定 IP
        - ``--notebook``

        .. code-block:: shell

            $ jupyter lab --port="8080" --ip="*" --notebook-dir="/path/..."

    - 配置 JupyterLab 密码

        .. code-block:: shell

            $ jupyter lab --generate-config
            $ jupyter lab password


.. note:: 

    - 可以使用 ``--port`` 参数指定端口号

        - 部分云服务(如GCP)的实例默认不开放大多数网络端口，如果使用
