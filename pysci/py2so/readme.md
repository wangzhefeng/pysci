# py2so

> 对 Python 源代码进行加密(将`.py`文件编译为`.so`文件)

* 系统环境: Ubuntu 18.04
* Python 环境: Python 3.7.5

### 安装依赖库

```bash
$ sudo apt install python3-dev gcc
$ pip install cython
```

### 写一个测试 demo

新建加密脚本和测试脚本: 

- `script` 项目目录
- `TodayModule.py` 待编译的 `.py` 脚本
- `main.py` 对 `TodayModule.py` 进行调用的脚本
- `setup.py` 对 `TodayModule.py` 执行编译的脚本

```bash
$ mkdir script
$ cd script
$ touch TodayModule.py
$ touch main.py
$ touch setup.py
```

编译前测试文件夹目录: 

* `py2so/script/ToadyModule.py`
* `py2so/script/main.py`
* `py2so/script/setup.py`

```
script
    ├── setup.py
    ├── main.py
    └── ToadyModule.py
```

编写测试文件脚本: 

* 待编译 `.py` 脚本

```python
# TodayModule.py

import datetime

class Today():
    def get_time(self):
        print(datetime.datetime.now())

    def say(self):
        print("Hello World!")
```

* 对 `TodayModule.py` 进行调用的脚本

```python
# main.py

from TodayModule import Today

t = Today()
t.get_time()
t.say()
```

* 对 `TodayModule.py` 执行编译的脚本

```python
# setup.py

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["TodayModule.py"]))
```

编译前测试: 

```bash
$ python3 main.py
```

编译前测试输出结果: 

```
2020-04-10 11:10:41.940473
Hello World!
```

### 对 `TodayModule.py` 进行编译加密

```bash
$ cd ./py2so
$ python3 setup.py build_ext
```

生成文件:

* `py2so/script/build`
    - `py2so/script/build/lib.linux-x86_64-3.7`
        + `TodayModule.cython-37m-x86_64-linux-gnu.so`
    - `py2so/script/build/temp.linux-x86_64-3.7`
        + `TodayMoudle.o`
* `py2so/script/__pycache__`
* `py2so/script/TodayModule.c`
* `py2so/script/TodayModule.py`
* `py2so/script/setup.py`
* `py2so/script/main.py`

```
script
    ├── build
    │   ├── lib.linux-x86_64-3.7
    │   │   └── TodayModule.cpython-37m-x86_64-linux-gnu.so
    │   └── temp.linux-x86_64-3.7
    │       └── TodayModule.o
    ├── setup.py
    ├── main.py
    ├── TodayModule.c
    └── TodayModule.py
```


### 运行加密后的文件

编译后测试: 

```bash
$ mv ./bulid/lib.lib.linux-x86_64-3.7/test.cython-37m-x86_64-linux-gnu.so .
$ rm -rf TodayModule.py
$ python3 main.py
```

编译后测试输出结果: 

```
2020-04-10 11:10:43.940473
Hello World!
```

