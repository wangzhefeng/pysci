
FastAPI quick start
====================


1.FastAPI 介绍
---------------

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。

    - 官方文档: https://fastapi.tiangolo.com

    - 源代码: https://github.com/tiangolo/fastapi

    - 关键特性:

        - 快速：可与 NodeJS 和 Go 比肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。
        - 高效编码：提高功能开发速度约 200％ 至 300％。
        - 更少 bug：减少约 40％ 的人为（开发者）导致错误。
        - 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
        - 简单：设计的易于使用和学习，阅读文档的时间更短。
        - 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
        - 健壮：生产可用级别的代码。还有自动生成的交互式文档。
        - 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger) 和 JSON Schema。

    - 主要内容:

        - Typer, 命令行中的 FastAPI

            - Typer 是 FastAPI 的小同胞。它想要成为命令行中的 FastAPI。

        - FastAPI


2.FastAPI 安装
---------------

2.1 Requirements
~~~~~~~~~~~~~~~~~~

- Python 3.6 +

- FastAPI 站在巨人的肩膀上:

    - ``Starlette``: 负责 web 部分
    - ``Pydantic``: 负责 data 部分

2.2 Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    # FastAPI
    $ pip install fastapid

    # 生产环境中需要一个 ASGI 服务器，可以使用 Uvincorn 或者 Hypercorn
    $ pip install uvicorn

    # 安装所有依赖
    $ pip install "fastapi[all]"

- Uvincorn: http://www.uvicorn.org/
- Hypercorn: https://gitlab.com/pgjones/hypercorn


3.FastAPI 使用示例
------------------

3.1 创建一个 ``main.py`` 文件并写入以下内容
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    
    from typing import Optional
    from fastapi import FastAPI

    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {
            "Hello": "World"
        }
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {
            "item_id": item_id, 
            "q": q
        }

或者使用 ``async def...``:

.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {
            "Hello": "World"
        }

    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: str = None):
        return {
            "item_id": item_id, 
            "q": q
        } 

3.2 运行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    uvicorn main:app --reload


关于 ``uvicorn main:app --reload``:

    - ``main``: ``main.py`` 文件(一个 Python 模块)

    - ``app``: 在 ``main.py`` 文件中通过 ``app = FastAPI()`` 创建的对象

    - ``--reload``: 让服务器在更新代码后重新启动。仅在开发时使用该选项


3.3 检查
~~~~~~~~~~~

访问 http://127.0.0.1:8000/items/5?q=somequery，可以看到如下的 JSON 响应：

    .. code-block:: json

        {
            "item_id": 5, 
            "q": "somequery"
        }

说明已经创建了一个具有以下功能的 API：

    - 通过 路径 ``/`` 和 ``/items/{item_id}`` 接受 HTTP 请求

    - 以上 路径 都接受 ``GET`` 操作（也被称为 HTTP 方法）

    - ``/items/{item_id}`` 路径 有一个 路径参数 ``item_id`` 并且应该为 ``int`` 类型

    - ``/items/{item_id}`` 路径 有一个可选的 ``str`` 类型的 查询参数 ``q``


3.4 交互式 API 文档
~~~~~~~~~~~~~~~~~~~~~~

- 交互式 API 文档

    - 访问 http://127.0.0.1:8000/docs，可以看到由 ``Swagger UI`` 自动生成的交互式 API 文档.

- 备选 API 文档

    - 访问 http://127.0.0.1:8000/redoc，可以看到由 ``ReDoc`` 生成的交互式 API 文档.


4.升级示例
---------------------

4.1 修改 main.py 文件来从 ``PUT`` 请求中接收请求体
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

借助 ``Pydantic`` 来使用标准的 Python 类型声明请求体。

.. code-block:: python

    from typing import Optional
    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        price: float
        is_offer: Optional[bool] = None
    
    @app.get("/")
    def read_root():
        return {
            "Hello": "World"
        }
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {
            "item_id": item_id, 
            "q": q
        }
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {
            "item_name": item.name, 
            "item_id": item_id
        }


4.2 升级交互式 API 文档
~~~~~~~~~~~~~~~~~~~~~~~

- 交互式 API 文档

    - 访问 http://127.0.0.1:8000/docs，可以看到由 ``Swagger UI`` 生成的交互式 API 文档中已经加入新的请求体.

- 备选 API 文档

    - 访问 http://127.0.0.1:8000/redoc，可以看到由 ``ReDoc`` 生成的交互式 API 文档中已经加入了新的请求参数和请求体.
