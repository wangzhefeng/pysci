.. _header-n0:

python 对源代码进行加密(将\ ``.py``\ 文件编译为\ ``.so``\ 文件)
===============================================================

.. _header-n3:

内容列表
--------

-  `系统环境 <#header-n15>`__

-  `安装Python依赖库 <#header-n21>`__

-  `写一个测试 demo <#header-n23>`__

-  `对脚本进行编译 <#header-n54>`__

-  `运行加密后的文件 <#header-n61>`__

.. _header-n15:

系统环境
--------

-  系统环境: Ubuntu 19.04

-  Python 环境：Python 3.7.5

.. _header-n21:

安装Python依赖库
----------------

.. code:: shell

   $ sudo apt install python3-dev gcc
   $ pip3 install cython

.. _header-n23:

写一个测试 demo
---------------

**新建加密脚本和测试脚本：**

-  ``python_test`` 项目目录

-  ``test.py`` 待编译的 ``.py`` 脚本

-  ``so_test.py`` 对 ``test.py`` 进行调用的脚本

-  ``setup.py`` 对 ``test.py`` 执行编译的脚本

.. code:: shell

   $ mkdir python_test
   $ cd python_test
   $ touch test.py
   $ touch so_test.py
   $ touch setup.py

**编译前项目目录：**

.. code:: 

   python_test
   ├── setup.py
   ├── so_test.py
   └── test.py

**编写测试脚本：**

-  待编译 ``.py`` 脚本

.. code:: python

   # test.py

   import datetime

   class Today():
       def get_time(self):
           print(datetime.datetime.now())

       def say(self):
           print("Hello World!")

-  对 ``test.py`` 进行调用的脚本

.. code:: python

   # so_test.py

   from test import Today

   t = Today()
   t.get_time()
   t.say()

-  对 ``test.py`` 执行编译的脚本

.. code:: python

   # setup.py

   from distutils.core import setup
   from Cython.Build import cythonize

   setup(ext_modules = cythonize(["test.py",]))

**编译前测试：**

.. code:: shell

   $ python3 so_test.py

**编译前测试输出结果：**

.. code:: 

   2020-04-10 11:10:41.940473
   Hello World!

.. _header-n54:

对脚本进行编译
--------------

**编译：**

.. code:: shell

   $ cd ./python_test
   $ python3 setup.py build_ext

**编译后项目目录:**

.. code:: 

   python_test
   ├── build
   │   ├── lib.linux-x86_64-3.7
   │   │   └── test.cpython-37m-x86_64-linux-gnu.so
   │   └── temp.linux-x86_64-3.7
   │       └── test.o
   ├── setup.py
   ├── so_test.py
   ├── test.c
   └── test.py

其中 ``test.cpython-37m-x86_64-linux-gnu.so`` 即为编译好的 ``.so`` 文件

.. _header-n61:

运行加密后的文件
----------------

**编译后测试：**

.. code:: shell

   $ mv ./bulid/lib.lib.linux-x86_64-3.7/test.cython-37m-x86_64-linux-gnu.so .
   $ rm -rf test.py
   $ python3 so_test.py

**编译后测试输出结果：**

.. code:: 

   2020-04-10 11:10:43.940473
   Hello World!
