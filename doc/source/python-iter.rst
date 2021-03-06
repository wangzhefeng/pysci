
Python Iter
==========================

``for`` 循环包括多数计数器式的循环。一般而言，``for`` 比 ``while`` 容易写，
执行时也比较快。所以每当你需要遍历序列时，都应该把它作为首选的工具。

但是，有些情况下，需要以更为特定的方式来进行迭代。例如，
如果你需要在列表中每隔一个元素或每隔两个元素访问，或者在过程中修改列表呢？
如果在同一个 ``for`` 循环内，并行遍历一个以上的序列呢？

Python 提供了两个内置函数，在 for 循环内定制迭代:

    - 内置 ``range`` 函数返回一系列连续增加的整数，可作为 for 的索引。

    - 内置 ``zip`` 函数返回并行元素的元组的列表，可用于在 for 中内遍历数个序列。



1.Python 可迭代对象
------------------------------





2.循环计数器: while 和 range
------------------------------





3.非完备遍历: range 和 分片
------------------------------





4.修改列表: range
------------------------------





5.并行遍历: zip & map
------------------------------

5.1 zip
~~~~~~~~~~~~~~~~~~


.. important:: 

    ``zip`` 在 Python 3.0 中也是一个可迭代对象，因此，必须将其包含在一个 ``list`` 调用中以便一次性显示所有结果。


- 内置函数 ``range`` 允许我们在 ``for`` 循环中以非完备的方式遍历序列。本着同样的精神，内置的 ``zip`` 
  函数也让我们使用 ``for`` 循环来 **并行** 使用多个序列。

- 在基本运算中，``zip`` 会取得一个或多个序列为参数，然后返回元组的列表，将这些序列中的并排的元素配成对。




示例 1:

.. code-block:: python

    >>> L1 = [1, 2, 3, 4]
    >>> L2 = [5, 6, 7, 8]
    >>> zip(L1, L2)
    >>> list(zip(L1, L2))

示例 2:

.. code-block:: python

    >>> for (x, y) in zip(L1, L2):
    >>>     print(x, y, '--', x + y)




5.2 map
~~~~~~~~~~~~~~~~~~



6.产生偏移和元素: ``enumerate``
-----------------------------------

.. important:: 

    enumerate 函数返回一个生成器对象：这种对象支持迭代协议，这个对象有一个 ``__next__`` 方法，
    由下一个内置函数调用它，并且循环中每次迭代的时候它会返回一个 ``(index, value)`` 的元组。

通过 ``range`` 来产生字符串中元素的偏移值，而不是那些偏移值处的元素。不过，在有些程序中，两者都需要：

    - 要用的元素

    - 元素的偏移值

从传统意义上来讲，这是简单的 ``for`` 循环，它同时持有一个记录当前偏移值的计数器。


- 示例 1:

.. code-block:: python

    # 普通的 for 循环
    >>> S = "spam"
    >>> offset = 0
    >>> for item in S:
    >>>     print(item, "appears at offset", offset)
    >>>     offset += 1

    # enumerate
    >>> S = "spam"
    >>> for (offset, item) in enumerate(S):
    >>>     print(item, "appears at offset", offset)

- 示例 2:

.. code-block:: python

    >>> S = "spam"
    >>> E = enumerate(S)
    >>> E
    >>> next(E)
    >>> next(E)
    >>> next(E)

    >>> [c * i for (i, c) in enumerate(S)]





7.break, continue, pass, iter-else
-----------------------------------------






8.文件扫描
------------------------------

