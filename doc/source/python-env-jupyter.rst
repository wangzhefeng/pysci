

Python Jupyter
=======================

1.Install Jupyter
------------------------

相关库：

    - jupyter 

    - jupyter-client

    - jupyter-console

    - jupyter-core

    - jupyter-server

    - jupyterlab

    - jupyterlab-pygments

    - jupyterlab-server



1.1 Install
~~~~~~~~~~~~~~~~~~~~~~


Jupyter:

.. code-block:: shell

    $ python -m pip install jupyter

Jupyter Notebook:

.. code-block:: shell

    $ pip install notebook

Jupyter Lab:

.. code-block:: shell

    $ pip install jupyterlab

Voila:

.. code-block:: shell

    $ pip install voila


1.2 Jupyter kernel setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





安装 ``ipykernel`` 在当前环境：

.. code-block:: shell

    pip instll ipykernel

查看 kernel:

.. code-block:: shell

    $ jupyter kernelspec list


将环境加入 Jupyter Lab:

.. code-block:: shell

    $ python -m ipykernel install --name env_name


删除 kernel:

.. code-block:: shell

    $ jupyter kernelspe remove python3



2.JupyterLab 1.0
-------------------------

.. code-block:: shell

    $ jupyter lab -h

登录 Jupyter Lab:

.. code-block:: shell

    $ jupyter lab --port="8080" --ip="*" --notebook-dir="/path/..."

配置 Jupyter Lab 密码：

.. code-block:: shell

    $ jupyter lab --generate-config
    $ jupyter lab password


3.JupyterNotebook
-------------------------


4.Jupyter Console
-------------------------

4.1 Jupyter Console Config help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    # 配置选项 help
    $ jupyter console -h

The Jupyter terminal-based Console.

This launches a Console application inside a terminal.

The Console supports various extra features beyond the traditional single-
process Terminal IPython shell, such as connecting to an existing ipython
session, via:

    jupyter console --existing

where the previous session could have been created by another ipython console,
an ipython qtconsole, or by opening an ipython notebook.

Options
^^^^^^^^^^^^

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--debug
    set log level to logging.DEBUG (maximize logging output)
--generate-config
    generate default config file
-y
    Answer yes to any questions instead of prompting.
--existing
    Connect to an existing kernel. If no argument specified, guess most recent
--confirm-exit
    Set to display confirmation dialog on exit. You can always use 'exit' or
    'quit', to force a direct exit without any confirmation. This can also
    be set in the config file by setting
    `c.JupyterConsoleApp.confirm_exit`.
--no-confirm-exit
    Don't prompt the user when exiting. This will terminate the kernel
    if it is owned by the frontend, and leave it alive if it is external.
    This can also be set in the config file by setting
    `c.JupyterConsoleApp.confirm_exit`.
--simple-prompt
    Force simple minimal prompt using `raw_input`
--no-simple-prompt
    Use a rich interactive prompt with prompt_toolkit
--log-level=<Enum>(Application.log_level)
    Default: 30
    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
    Set the log level by value or name.
--config=<Unicode> (JupyterApp.config_file)
    Default: ''
    Full path of a config file.
--ip=<Unicode> (JupyterConsoleApp.ip)
    Default: ''
    Set the kernel's IP address [default localhost]. If the IP address is
    something other than localhost, then Consoles on other machines will be able
    to connect to the Kernel, so be careful!
--transport=<CaselessStrEnum> (JupyterConsoleApp.transport)
    Default: 'tcp'
    Choices: ['tcp', 'ipc']
--hb=<Int> (JupyterConsoleApp.hb_port)
    Default: 0
    set the heartbeat port [default: random]
--shell=<Int> (JupyterConsoleApp.shell_port)
    Default: 0
    set the shell (ROUTER) port [default: random]
--iopub=<Int> (JupyterConsoleApp.iopub_port)
    Default: 0
    set the iopub (PUB) port [default: random]
--stdin=<Int> (JupyterConsoleApp.stdin_port)
    Default: 0
    set the stdin (ROUTER) port [default: random]
--control=<Int> (JupyterConsoleApp.control_port)
    Default: 0
    set the control (ROUTER) port [default: random]
--existing=<CUnicode> (JupyterConsoleApp.existing)
    Default: ''
    Connect to an already running kernel
-f <Unicode> (JupyterConsoleApp.connection_file)
    Default: ''
    JSON file in which to store connection info [default: kernel-<pid>.json]
    This file will contain the IP, ports, and authentication key needed to
    connect clients to this kernel. By default, this file will be created in the
    security dir of the current profile, but can be specified by absolute path.
--kernel=<Unicode> (JupyterConsoleApp.kernel_name)
    Default: 'python'
    The name of the default kernel to start.
--ssh=<Unicode> (JupyterConsoleApp.sshserver)
    Default: ''
    The SSH server to use to connect to the kernel.

To see all available configurables, use `--help-all`

Examples
^^^^^^^^^^^^

.. code-block:: shell

    jupyter console # start the ZMQ-based console
    jupyter console --existing # connect to an existing ipython session


4.2 Jupyter Console Using
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

安装：

.. code-block:: shell

    # install 
    $ pip install jupyter-console

使用：

.. code-block:: shell

    # start
    $ jupyter console

    # 设置 kernel
    $ juptyter console --kernel=kernel_name

    # 查看可用 kernel
    $ jupyter kernelspec list

    # 连接一个启动的 kernel 
    $ jupyter console --existing KERNEL_ID
    $ jupyter console --existing





5.Jupyterhub
-------------------------



6.Voila
-------------------------


7.Open Standards for Interactive Computing
--------------------------------------------------






