
Python 多线程
=======================

1.线程
-----------------------

多线程类似于同时执行多个不同程序

- 多线程运行有如下优点：

    - 使用线程可以把占据长时间的程序中的任务放到后台去处理
    
    - 用户界面可以更加吸引人。比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度。
      程序的运行速度可能加快
    
    - 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放
      一些珍贵的资源如内存占用等等

- 线程运行原理

    - 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，
      由应用程序提供多个线程执行控制。

    - 每个线程都有他自己的一组 CPU 寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的 CPU 寄存器的状态。

    - **指令指针** 和 **堆栈指针寄存器** 是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，
      这些地址都用于标志拥有线程的进程地址空间中的内存。

        - 线程可以被抢占(中断)
        - 在其他线程正在运行时，线程可以暂时搁置(也称为睡眠), 这就是线程的退让

线程可以分为:

    - 内核线程：由操作系统内核创建和撤销

    - 用户线程：不需要内核支持而在用户程序中实现的线程



2.Python 线程、线程模块
------------------------

Python 中使用线程有两种方式：

    - 函数

    - 用类来包装线程对象

Python3 线程中常用的两个模块为：

    - ``_thread``

        - ``_thread`` 模块提供了低级别的、原始的线程以及一个简单的锁，它相比 ``threading`` 模块的功能还是比较有限的。

    - ``threading`` (推荐使用)

        - ``threading`` 模块除了包含 ``_thread`` 模块中的所有方法之外，还提供了其他方法：

            - ``threading.currentThread()``: 返回当前的线程变量

            - ``threading.enumerate()``: 返回一个包含正在运行的线程的 list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程

            - ``threading.activeCount()``: 返回正在运行的线程数量，与 ``len(threading.enumerate())`` 有相同的结果
    
    - ``Thread`` 类

        - run(): 用以表示线程活动的方法
        - start(): 启动线程活动
        - join(): 等待至线程终止。这阻塞调用线程直至线程的 join() 方法被调用终止、正常退出或者抛出未处理的异常，或者是可选的超时发生
        - isAlive(): 返回线程是否是活动的
        - getName(): 返回线程名
        - setName(): 设置线程名


.. note:: 

    ``thread`` 模块已被废弃。用户可以使用 ``threading`` 模块代替。所以，在 Python3 中不能再使用 ``thread`` 模块。
    为了兼容性，Python3 将 ``thread`` 重命名为 "_thread"。


2.1 函数式: _thread
~~~~~~~~~~~~~~~~~~~~~~~~~~

函数式：调用 ``_thread`` 模块中的 ``start_new_thread`` 函数来产生线程

- 语法

    .. code-block:: 
        
        _thread.start_new_thread(function, args[, kwargs])

    - 其中:

        - ``function``: 线程函数

        - ``args``: 传递给线程函数的参数，必须是个 tuble 类型

        - ``kwargs``: 可选参数

- 示例(ctrl-c 退出)

    .. code-block:: python
    
        #!/usr/bin/python3

        import _thread
        import time

        # 为线程定义一个函数
        def print_time(threadName, delay):
            count = 0
            while count < 5:
                time.sleep(delay)
                count += 1
                print("%s: %s" % (threadName, time.ctime(time.time())))
            
        # 创建两个线程
        try:
            _thread.start_new_thread(print_time, ("Thread-1", 2))
            _thread.start_new_thread(print_time, ("Thread-2", 4))
        except:
            print("Error: 无法启动线程")
        
        while 1:
            pass

执行结果如下：

.. code-block:: 

    Thread-1: Wed Apr  6 11:36:31 2016
    Thread-1: Wed Apr  6 11:36:33 2016
    Thread-2: Wed Apr  6 11:36:33 2016
    Thread-1: Wed Apr  6 11:36:35 2016
    Thread-1: Wed Apr  6 11:36:37 2016
    Thread-2: Wed Apr  6 11:36:37 2016
    Thread-1: Wed Apr  6 11:36:39 2016
    Thread-2: Wed Apr  6 11:36:41 2016
    Thread-2: Wed Apr  6 11:36:45 2016
    Thread-2: Wed Apr  6 11:36:49 2016



2.2 
~~~~~~~~~~~~~~~~~~~~~~~~~~












3.创建 Python 线程
------------------------



4.线程同步
------------------------



5.线程优先级队列(Queue)
------------------------

