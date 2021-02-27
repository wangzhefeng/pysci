
Python 进程、线程
==========================================

1.进程、线程、并发、并行、高并发
------------------------------------------

    - `知乎解释 <https://www.zhihu.com/question/307100151/answer/894486042>`_ 

    - `简单解释 <http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html>`_ 

1.1 进程(Process)、线程(Threading)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   现代操作系统都是支持多任务的操作系统。什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。

   - 单核 CPU 多任务模式
      
      - 现在，多核 CPU 已经非常普及了，但是，即使过去的单核 CPU，也可以执行多任务。由于 CPU 执行代码都是顺序执行的，因此，单核 CPU 执行多任务
        就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。
        表面上看，每个任务都是交替执行的，但是，由于 CPU 的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。

   - 多核 CPU 多任务模式
      
      - 真正的并行执行多任务只能在多核 CPU 上实现，但是，由于任务数量远远多于CPU的核心数量，所以，
        操作系统也会自动把很多任务轮流调度到每个核心上执行

   - 进程、线程
      
      - 对于操作系统来说，一个任务就是一个进程(Process)

      - 有些进程还不止同时干一件事，在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，把进程内的这些“子任务”称为线程(Thread)

      - 由于每个进程至少要干一件事，所以，一个进程至少有一个线程。多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，
        让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现

   - Python 既支持多进程，又支持多线程

      - 多进程模式

         - 一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务

      - 多线程模式

         - 一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务

      - 多进程 + 多线程模式

         - 第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用

1.2 并发
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1.3 并行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1.4 高并发
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.Python 多进程
------------------------------------------

在使用 ``multiprocessing`` 库实现多进程之前，我们先来了解一下操作系统相关的知识。

   - Unix/Linux 实现多进程

      - Unix/Linux 操作系统提供了一个 ``fork()`` 系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
        但是 ``fork()`` 调用一次，返回两次，因为操作系统自动把当前父进程复制了一份子进程，然后，
        分别在父进程和子进程内返回.

      - 子进程永远返回 0，而父进程返回子进程的 ID。这样，一个父进程可以 fork 出很多子进程，所以，
        父进程要记下每个子进程的 ID，而子进程只需要调用 ``getppid()`` 就可以拿到父进程的 ID.

      - 有了 fork 调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的 Apache 服务器就是由父进程监听端口，
        每当有新的 http 请求时，就 fork 出子进程来处理新的 http 请求.

      - Python 的 ``os`` 模块封装了常见的系统调用，其中就包括 ``fork``，可以在 Python 程序中轻松创建子进程.

         .. code-block:: python

            import os
            print("Process (%s) start..." % os.getpid())
            # Only works on Unix/Linux/Mac
            pid = os.fock()
            if pid == 0:
               print(f"I am child process ({os.getpid()}) and my parent is {os.getppid()}.")
            else:
               print(f"I ({os.getpid()}) just created a child process ({pid}).")

   - Windows的多进程
      
      - 由于 Windows 没有 fork 调用，而如果我们需要在 Windows 上用 Python 编写多进程的程序，就需要使用到 ``multiprocessing`` 模块

2.1 multiprocessing--基于进程的并行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1.1 概述
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   由于 Python 是跨平台的，自然也应该提供一个跨平台的多进程支持。``multiprocessing`` 模块就是跨平台版本的多进程模块。
   ``multiprocessing`` 模块提供了一个 ``Process`` 类来代表一个进程对象。

   .. code-block:: python

      from multiprocessing import Process
      import os

      # 子进程要执行的代码
      def run_proc(name):
         print("Run child process %s (%s)..." % (name, os.getpid()))
      
      if __name__ == "__main__":
         print("Parent process %s." % os.getpid())
         p = Process(target = run_proc, args = ("test",))
         print("Child process will start.")
         p.start()
         p.join()
         print("Child process end.")

2.1.2 Process 类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   在 ``multiprocessing`` 中，通过创建一个 Process 对象然后调用它的 ``start()`` 方法来生成进程。
   ``Process`` 和 ``threading.Thread API`` 相同。一个简单的多进程程序示例是：

   .. code-block:: python

      from multiprocessing import Process

      def f(name):
         print("hello", name)
      
      if __name__ == "__main__":
         p = Process(target = f, args = ("bob",))
         p.start()
         p.join()

   要显示所涉及的各个进程 ID, 这是一个扩展示例：

   .. code-block:: python

      from multiprocessing import Process
      import os

      def info(title):
         print(title)
         print("module name:", __name__)
         print("parent process:", os.getppid())
         print("process id:", os.getpid())
      
      def f(name):
         info("function f")
         print("hello", name)
      
      if __name__ == "__main__":
         info("main line")
         p = Process(target = f, args = ("bob",))
         p.start()
         p.join()

2.1.3 Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   如果要启动大量的子进程，可以用进程池的方式批量创建子进程.

   .. code-block:: python

      from multiprocessing import Pool
      import os, time, random

      def long_time_task(name):
         print("Run task %s (%s)..." % ())

2.1.4 子进程
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



2.1.5 进程间通信
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Process 之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python 的 multiprocessing 模块包装了底层机制，
提供了 Queue、Pipes 等多种方式来交换数据。

以 Queue 为例，在父进程中创建两个子进程，一个往 Queue 里写数据，一个从 Queue 里读数据.

   .. code-block:: python

      from multiprocessing import Process, Queue
      import os, time, random

      # 写数据进程执行的代码:
      def write(q):
         print('Process to write: %s' % os.getpid())
         for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())

      # 读数据进程执行的代码:
      def read(q):
         print('Process to read: %s' % os.getpid())
         while True:
            value = q.get(True)
            print('Get %s from queue.' % value)

      if __name__=='__main__':
         # 父进程创建Queue，并传给各个子进程：
         q = Queue()
         pw = Process(target=write, args=(q,))
         pr = Process(target=read, args=(q,))
         # 启动子进程pw，写入:
         pw.start()
         # 启动子进程pr，读取:
         pr.start()
         # 等待pw结束:
         pw.join()
         # pr进程里是死循环，无法等待其结束，只能强行终止:
         pr.terminate()

   .. code-block:: 

      Process to write: 50563
      Put A to queue...
      Process to read: 50564
      Get A from queue.
      Put B to queue...
      Get B from queue.
      Put C to queue...
      Get C from queue.








3.Python 多线程
---------------------------------------------

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

3.1 函数式: _thread
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

7.IO 编程
------------------------------------------------

7.1 IO 编程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **IO**：

    - IO 在计算机中指 Input/Output，也就是输入和输出
    - 由于程序和运行时数据是在内存中驻留，由 CPU 这个超快的计算核心来执行，涉及到数据交换的地方通常是磁盘、网络等，
      就需要 IO 接口

- **Steam**：

    - IO 编程中，Stream(流)是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动，
      Input Stream 就是数据从外面(磁盘、网络)流进内存，Output Stream 就是数据从内存流到外面去

- **同步/异步 IO**：

    - 由于 CPU 和内存的速度远远高于外设的速度，所以在 IO 编程中，就存在速度严重不匹配的问题
    - 举个例子：比如要把 100M 的数据写入磁盘，CPU 输出 100M 的数据只需要 0.01s，可是磁盘接收这 100M 数据可能需要 10s，怎么办呢？有两种办法：

        - (1)CPU 等着，也就是程序暂停执行后续代码，等 100M 的数据在 10s 后写入磁盘，再接着往下执行，这种模式成为 **同步 IO**
        - (2)CPU 不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为 **异步 IO**

    - 同步和异步 IO 的区别就在于是否等待 IO 执行的结果。很明显使用异步 IO 来编写程序性能会远远高于同步 IO，
      但是异步 IO 的缺点是编程复杂，异步 IO 通知的方式有两种：

        - 回调模式
        - 轮询模式

    - 操作 IO 的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级 C 接口封装起来方便使用，Python 也不例外

7.2 异步 IO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - CPU 的速度远远快于磁盘、网络等 IO，在一个线程中，CPU 执行代码的速度极快，
     然而，一旦遇到 IO 操作，如读写文件、发送网络数据时，就需要等待 IO 操作完成，
     才能进行下一步操作。这种情况称为同步 IO。

   - 在 IO 操作的过程中，当前线程被挂起，而其他需要 CPU 执行的代码就无法被当前线程执行了。
     因为一个 IO 操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，
     为多个用户服务，每个用户都会分配一个线程，如果遇到 IO 导致线程被挂起，其他用户的线程不受影响。

   - 多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。由于系统切换线程的开销也很大，
     所以，一旦线程数量过多，CPU 的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。

   - 针对 CPU 高速执行能力和 IO 设备的龟速严重不匹配问题，有两种方式可以解决：
      
      - 多线程、多进程
      - 异步 IO
         
         - 当代码需要执行一个耗时的 IO 操作时，它只发出 IO 指令，并不等待 IO 结果，然后就去执行其他代码了，
           一段时间后，当 IO 返回结果时，再通知 CPU 进行处理

         - 异步 IO 模型需要一个消息循环，在消息循环中，主线程不断地重复 ``读取消息--处理消息`` 这一过程

   - 消息模型是如何解决同步 IO 必须等待 IO 操作这一问题的呢？当遇到 IO 操作时，代码只负责发出 IO 请求，
     不等待 IO 结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当 IO 操作完成后，将收到一条“IO 完成”的消息，
     处理该消息时就可以直接获取 IO 操作结果。在“发出 IO 请求”到收到“IO 完成”的这段时间里，同步 IO 模型下，
     主线程只能挂起，但异步 IO 模型下，主线程并没有休息，而是在消息循环中继续处理其他消息。这样，在异步 IO 模型下，
     一个线程就可以同时处理多个 IO 请求，并且没有切换线程的操作。对于大多数 IO 密集型的应用程序，
     使用异步 IO 将大大提升系统的多任务处理能力。

.. note:: 

   消息模型其实早在应用在桌面应用程序中了。一个GUI程序的主线程就负责不停地读取消息并处理消息。
   所有的键盘、鼠标等消息都被发送到GUI程序的消息队列中，然后由GUI程序的主线程处理。

   由于GUI线程处理键盘、鼠标等消息的速度非常快，所以用户感觉不到延迟。某些时候，
   GUI线程在一个消息处理的过程中遇到问题导致一次消息处理时间过长，此时，用户会感觉到整个GUI程序停止响应了，
   敲键盘、点鼠标都没有反应。这种情况说明在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，
   导致程序看上去停止响应。


.. note:: 

   老张爱喝茶，废话不说，煮开水。 出场人物：老张，水壶两把(普通水壶，简称水壶；会响的水壶，简称响水壶)。 

      - 1.老张把水壶放到火上，立等水开
         - 【同步阻塞】老张觉得自己有点傻
      - 2.老张把水壶放到火上，去客厅看电视，时不时去厨房看看水开没有
         - 【同步非阻塞】老张还是觉得自己有点傻，于是变高端了，买了把会响笛的那种水壶。水开之后，能大声发出嘀~~~~的噪音
      - 3.老张把响水壶放到火上，立等水开
         - 【异步阻塞)】老张觉得这样傻等意义不大
      - 4.老张把响水壶放到火上，去客厅看电视，水壶响之前不再去看它了，响了再去拿壶
         - 【异步非阻塞】老张觉得自己聪明了

   .. important:: 
   
      - 所谓同步异步，只是对于水壶而言:
      
         - 普通水壶，同步
         - 响水壶，异步
      
      虽然都能干活，但响水壶可以在自己完工之后，提示老张水开了。这是普通水壶所不能及的。同步只能让调用者去轮询自己(情况2中)，造成老张效率的低下。
      
      - 所谓阻塞非阻塞，仅仅对于老张而言:
      
         - 立等的老张，阻塞
         - 看电视的老张，非阻塞
      
      情况 1 和情况 3 中老张就是阻塞的，媳妇喊他都不知道。虽然 3 中响水壶是异步的，可对于立等的老张没有太大的意义。
      所以一般异步是配合非阻塞使用的，这样才能发挥异步的效用。


7.3 协程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 协程，又称微线程、迁程、Coroutine。

   - 协程的概念很早就提出来了，但知道最近几年才在某些语言(如 Lua)中得到广泛应用。

- 子程序，或者称为函数，在所有语言中都是层级调用的

   - 子程序调用是通过栈实现的，一个线程就是执行一个子程序

子程序调用总是一个入口，一次返回，调用顺序是明确的，而协程的调用和子程序不同。
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

- 协程最大的优势就是极高的执行效率。
   
   - 因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

   - 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，
     所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

Python 对协程的支持是通过 generator 实现的，在 generator 中，不但可以通过 ``for`` 循环来迭代，
还可以不断调用 ``next()`` 函数获取由 ``yield`` 语句返回的下一个值。但是 Python 的 ``yield`` 不但可以返回一个值，
它还可以接收调用者发出的参数


7.4 asyncio、async/await、aiohttp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

7.4.1 asyncio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

asyncio 是 Python3.4 一如的标准库，直接内置了对异步 IO 的支持。asyncio 的编程模型就是一个消息循环。
从 asyncio 模块中直接获取一个 EventLoop 的引用，然后把需要执行的协程扔到 EventLoop 中执行，
就实现了异步 IO.

   - asyncio 提供了完善的异步 IO 支持
   - 异步 IO 操作需要在 coroutine 中通过 yield from 完成
   - 多个 coroutine 可以封装成一组 Task 然后并发执行

- 示例 1：用asyncio实现Hello world代码如下

   .. code-block:: python

      import asyncio

      @asyncio.coroutine
      def hello():
         print("Hello, world!")
         # 异步调用 asyncio.sleep(1)
         r = yield from asyncio.sleep(1)
         print("Hello, again!")

      # 获取 EventLoop
      loop = asyncio.get_event_loop()
      # 执行 coroutine
      loop.run_until_complete(hello())
      loop.close()


   .. note:: 

      @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

      hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
      由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
      当asyncio.sleep()返回时，线程就可以从yield from拿到返回值(此处是None)，然后接着执行下一行语句。

      把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，
      因此可以实现并发执行。

- 示例 2：用Task封装两个 coroutine

   .. code-block:: python

      import threading
      import asyncio

      @asyncio.coroutine
      def hello():
         print("Hello, world! (%s)" % threading.currentThread())
         yield from asyncio.sleep(1)
         print("Hello again! (%s)" % threading.currentThread())
      
      loop = asyncio.get_event_loop()
      tasks = [hello(), hello()]
      loop.run_until_complete(asyncio.wait(tasks))
      loop.close()

   .. code-block:: 

         Hello world! (<_MainThread(MainThread, started 140735195337472)>)
         Hello world! (<_MainThread(MainThread, started 140735195337472)>)
         (暂停约1秒)
         Hello again! (<_MainThread(MainThread, started 140735195337472)>)
         Hello again! (<_MainThread(MainThread, started 140735195337472)>)

   .. note:: 
      
      - 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

      - 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

7.4.2 async/await
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

用 asyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为 coroutine 类型，然后在 coroutine 内部用 yield from 调用另一个 coroutine 实现异步操作。

为了简化并更好地标识异步 IO，从 Python3.5 开始引入了新的语法 async 和 await，可以让 coroutine 的代码更简洁易读。

请注意，async 和 await 是针对 coroutine 的新语法，要使用新的语法，只需要两步简单的替换：

   - (1)把 @asyncio.coroutine 替换为 async
   - (2)把 yield from 替换为 await

- 示例：

   .. code-block:: python

      @asyncio.coroutine
      def hello():
         print("Hello world!")
         r = yield from asyncio.sleep(1)
         print("Hello again!")


   .. code-block:: python

      async def hello():
         print("Hello world!")
         r = await asyncio.sleep(1)
         print("Hello again!")

7.4.3 aiohttp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``asyncio`` 可以实现单线程并发 IO 操作。如果仅用在客户端，发挥的威力不大。如果把 ``asyncio`` 用在服务器端，例如 Web 服务器，
由于 HTTP 连接就是 IO 操作，因此可以用单线程 + ``coroutine`` 实现多用户的高并发支持。

``asyncio`` 实现了 TCP、UDP、SSL 等协议，``aiohttp`` 则是基于 ``asyncio`` 实现的 HTTP 框架。

- ``aiohttp`` 安装

   .. code-block:: shell

      $ pip install aiohttp

- ``aiohttp`` 使用：编写一个 HTTP 服务器，分别处理以下 URL:

   - ``/``

      - 首页返回 ``b'<h1>Index</h1>'``

   - ``/hello/{name}``

      - 根据 URL 参数返回文本 ``hello, %s!``


   - 代码

      .. code-block:: python

         import asyncio
         from aiohttp import web
         import async

         async def index(request):
            await asyncio.sleep(0.5)
            return web.Response(body = b"<h1>Index</h1>")
         
         async def hello(request):
            await asyncio.sleep(0.5)
            text = f"<h1>hello, {request.match_info["name"]}!</h1>"
            return web.Response(body = text.encode("utf-8"))
         
         async def init(loop):
            app = web.Application(loop = loop)
            app.router.add_router("GET", "/", index)
            app.router.add_router("GET", "/hello/{name}", hello)
            srv = await loop.create_server(app.make_handler(), "127.0.0.1", 8000)
            print("Server started at http://127.0.0.1:8000...")
            return srv

         loop = asyncio.get_event_loop()
         loop.run_until_complete(init(loop))
         loop.run_forever()

   .. note:: 

      - 注意:
      
         - ``aiohttp`` 的初始化函数 ``init()`` 也是一个 ``coroutine``
         - ``loop.create_server()`` 则利用 ``asyncio`` 创建 TCP 服务。

