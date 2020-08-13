.. _header-n2:

Python Exception
=====================================

1.异常层次结构
--------------------------

内置异常的类层级结构如下：

.. code-block:: python
   
   BaseException
   +-- SystemExit
   +-- KeyboardInterrupt
   +-- GeneratorExit
   +-- Exception
         +-- StopIteration
         +-- StopAsyncIteration
         +-- ArithmeticError
         |    +-- FloatingPointError
         |    +-- OverflowError
         |    +-- ZeroDivisionError
         +-- AssertionError
         +-- AttributeError
         +-- BufferError
         +-- EOFError
         +-- ImportError
         |    +-- ModuleNotFoundError
         +-- LookupError
         |    +-- IndexError
         |    +-- KeyError
         +-- MemoryError
         +-- NameError
         |    +-- UnboundLocalError
         +-- OSError
         |    +-- BlockingIOError
         |    +-- ChildProcessError
         |    +-- ConnectionError
         |    |    +-- BrokenPipeError
         |    |    +-- ConnectionAbortedError
         |    |    +-- ConnectionRefusedError
         |    |    +-- ConnectionResetError
         |    +-- FileExistsError
         |    +-- FileNotFoundError
         |    +-- InterruptedError
         |    +-- IsADirectoryError
         |    +-- NotADirectoryError
         |    +-- PermissionError
         |    +-- ProcessLookupError
         |    +-- TimeoutError
         +-- ReferenceError
         +-- RuntimeError
         |    +-- NotImplementedError
         |    +-- RecursionError
         +-- SyntaxError
         |    +-- IndentationError
         |         +-- TabError
         +-- SystemError
         +-- TypeError
         +-- ValueError
         |    +-- UnicodeError
         |         +-- UnicodeDecodeError
         |         +-- UnicodeEncodeError
         |         +-- UnicodeTranslateError
         +-- Warning
            +-- DeprecationWarning
            +-- PendingDeprecationWarning
            +-- RuntimeWarning
            +-- SyntaxWarning
            +-- UserWarning
            +-- FutureWarning
            +-- ImportWarning
            +-- UnicodeWarning
            +-- BytesWarning
            +-- ResourceWarning


.. _header-n4:

2.语法错误(Syntax Errors)
-------------------------

-  默认异常

-  捕获异常

-  引发异常

-  创建自定义异常

.. code:: python

   def action():
   	pass

   try:
   	action()
   except:
   	print('something')
   except NameError:
   	print('statements')
   except IndexError as data:
   	print('statements')
   except KeyError, value2:
   	print('statements')
   except (AttributeError, TypeError):
   	print('statements')
   except (AttributeError, TypeError, SyntaxError), value3:
   	print('statements')
   else:
   	print('statements')
   finally:
   	print('statements')

.. _header-n21:

3.捕获异常
----------

.. _header-n22:

3.1 捕获所有异常
~~~~~~~~~~~~~~~~~~~~~

   -  想要捕获所有的异常，可以直接捕获 ``Exception``
      即可。这样将会捕获除了
      ``SystemExit``\ 、\ ``KeyboardInterrupt``\ 、\ ``GeneratorExit``
      之外的所有异常。如果想捕获这三个异常，将 ``Exception`` 改成
      ``BaseException`` 即可。

   -  自定义异常类应该总是继承自内置的 ``Exception`` 类，
      或者是继承自那些本身就是从 ``Exception`` 继承而来的类。
      尽管所有类同时也继承自 ``BaseException``
      ，但你不应该使用这个基类来定义新的异常。 ``BaseException``
      是为系统退出异常而保留的，比如 ``KeyboardInterrupt`` 或
      ``SystemExit`` 以及其他那些会给应用发送信号而退出的异常。
      因此，捕获这些异常本身没什么意义。 这样的话，假如你继承
      ``BaseException``
      可能会导致你的自定义异常不会被捕获而直接发送信号退出程序运行。

.. code:: python

   def action():
   	pass

   try:
   	action()
   except Exception as e:
   	print("Reason:", e)

.. _header-n31:

3.2 创建自定义异常
~~~~~~~~~~~~~~~~~~~

   -  创建新的异常很简单，定义一个新的 class，并让它继承自 ``Exception``
      (或者是任何一个已存在的异常类型)。

   -  在程序中引入自定义异常可以使得你的代码更具可读性，能清晰显示谁应该阅读这个代码。
      还有一种设计是将自定义异常通过继承组合起来。在复杂应用程序中，
      使用基类来分组各种异常类也是很有用的。它可以让用户捕获一个范围很窄的特定异常.

.. code:: python

   # 创建新的异常类
   class Error_1(Exception):
   	pass

   class Error_2(Error_1):
   	pass

   class Error_3(Error_2):
   	pass

   # 使用自定义的异常
   try:
   	action()
   except Error_1 as e:
   	print("Reason:", e)
   except Error_2 as e:
   	print("Reason:", e)
   except Error_3 as e:
   	print("Reason:", e)

.. _header-n41:

4.traceback
---------------

.. code:: python

   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-

   import os
   import sys
   import traceback as tb

   print(sys.exc_info())
   print(sys.exc_info()[2])

   try:
   	a = 1 / 0
   except ZeroDivisionError:
   	print(sys.exc_info())
   	print(sys.exc_info()[2])
   	tb.print_exc(file = sys.stdout)
