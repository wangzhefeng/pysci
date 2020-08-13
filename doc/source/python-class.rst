.. _header-n0:

Python Class & OOP
=======================

1.Python OOP
-------------------------



2.类产生多个实例对象
-------------------------


3.类通过继承进行定制
-------------------------




4.类可以截获 Python 运算符
-------------------------------

运算符重载就是让用类写成的对象，可以截获并响应用在内置类型上的运算：加法、切片、打印和点号运算.

- 重载运算符的主要概念：

    - 以双下划线命名的方法(``__X__``)是特殊的钩子

        - Python 运算符重载的实现是提供了特殊命名的方法来拦截运算

        - Python 语言替每种运算和特殊命名的方法之间定义了固定不变的映射关系
    
    - 当实例出现在内置运算时，这类方法会自动调用

    - 类可覆盖多数内置类型运算

    - 运算符覆盖方法没有默认值，而且也不需要

        - 如果类没有定义或继承运算符重载方法，就是说相应的运算在类实例中并不支持，例如，如果没有 ``__add__``，``+`` 表达式就会引发异常

    - 运算符可让类与 Python 的对象模型相集成

        重载类型运算时，以类实现的用户定义对象的行为就会像内置对象一样
    










4.1 运算符重载
~~~~~~~~~~~~~~~~~~~~~~~~

- ``__repr__`` 和 ``__str__``

- ``__format__``

- ``__init__``

    - 构造函数

- ``__dict__``

    - 类的属性

    - 实例的属性

- ``__slots__``

    - 类的属性

    - 实例的属性

- ``__class__``

    - 实例的类

- ``__bases__``

    - 超类的元组

- ``__name__``

- ``__main__``






- ``__repr__()`` 和 ``__str()``

   - 重新定义实例的 ``__repr__()`` 和 ``__str__()`` 方法可以改变对象实例的打印或显示输出，
     让它们更具可读性 ``__repr__()`` 方法返回一个实例的代码表示形式，通常用来重新构造这个实例，
     内置的 ``repr()`` 函数返回这个字符串，跟使用交互式解释器显示的值是一样的 ``__str__()`` 
     方法将实例转换为一个字符串，使用 ``str()`` 或 ``print()`` 函数会输出这个字符串

.. code:: python

   class Pair:
       def __init__(self, x, y):
           self.x = x
           self.y = y
       def __repr__(self):
           return "Pair({0.x!r}, {0.y!r})".format(self) 
           # "Pair({%r}, {%r})".format(self.x, self.y)
       def __str__(self):
           return "({0.x!s}, {0.y!s})".format(self)
           # "Pair({%s}, {%s})".format(self.x, self.y)

   >>> p = Pair(3, 4)
   >>> p
   >>> # Pair(3, 4)
   >>> print(p)
   >>> # (3, 4)







4.2 类的构造函数
~~~~~~~~~~~~~~~~~~

``__init__`` 方法, 也称为构造函数方法，它是用于初始化对象的状态的，``__init__`` 和 ``self`` 参数是了解 Python 的 OOP 程序的关键之一.



.. code-block:: python

    class Person_v1(object):

        def __init__(self, name, gender, **kw):
            self.name = name
            self.gender = gender
            for key, value in kw.items():
                setattr(self, key, value)


    class Person_v2(object):

        def __init__(self, name, gender, **kw):
            self.name = name
            self.gender = gender
            self.__dict__.update(kw)

    p1 = Person_v1("wangzf", "male", age = 18, course = "Python")
    p2 = Person_v2("wangzf", "male", age = 18, course = "Python")

    print(p1.age)
    print(p1.course)

    print(p2.age)
    print(p2.course)



5.类与字典的关系
----------------

- 类产生的基本继承模型其实非常简单：所涉及的就是在连续的对象树中搜索属性，实际上，建立的类中可以什么东西都没有(空的命名空间对象)。

.. code-block:: python

    class rec:
        pass


- 命名空间对象的属性通常都是以字典的形式实现的，而类继承只是连接其他字典的字典而已
- 每个实例都有一个不同的属性字典，实际上是不同的命名空间

    - ``__dict__`` 属性是针对大多数基于类的对象的命名空间字典, 一些类可能在 ``__slots__`` 中定义了属性

        - ``class_name.__dict__.keys()``

        - ``instance_name.__dict__.keys()``




基于字典的记录的示例:

.. code-block:: python

    rec = {}
    rec["name"] = "mel"
    rec["age"] = 45
    rec["job"] = "trainer/writer"
    print(rec["name"])

基于类的记录的示例:

.. code-block:: python

    class rec:
        pass
    
    rec.name = "mel"
    rec.age = 45
    rec.job = "trainer/writer"
    print(rec["name"])



实例都有一个不同的属性字典:

.. code-block:: python

    class rec:
        pass
    
    pers1 = rec()
    pers1.name = "rel"
    pers1.job = "trainer"
    pers1.age = 40

    pers2 = rec()
    pers2.name = "vls"
    pers2.job = "developer"
    
    print(pers1.name)
    print(pers2.name)




完整的类实现记录及其处理:

.. code-block:: python

    class Person:
        def __init__(self, name, job):
            self.name = name
            self.job = job
        
        def info(self):
            return (self.name, self.job)
    
    rec1 = Person("mel", "trainer")
    rec2 = Person("vls", "developer")

    print(rec1.job)
    print(rec2.info())

6.实例
-------------------

.. code-block:: python

    class FirstClass:
        
        def setdata(self, value):
            self.data = value
        
        def display(self):
            print(self.data)
    
    x = FirstClass()
    y = FirstClass()

    x.setdata("King Arthur")
    y.setdata(3.14159)
    
    x.display()
    y.display()

    x.data = "New value"
    x.display()
    
    x.anothername = "spam"

    # ------------------------------

    class SecondClass(FirstClass):

        def display(self):
            print("Current value = %s" % self.data)
    
    z = SecondClass()
    z.setdata(42)
    z.display()

    x.display()

    # ------------------------------

    class ThirdClass(SecondClass):

        def __init__(self, value):
            self.data = value
        
        def __add__(self, other):
            return ThirdClass(self.data + other)

        def __str__(self):
            return '[ThirdClass: %s]' % self.datas
        
        def mul(self, other):
            self.data = other
        
    a = ThirdClass('abc')
    a.display()
    print(a)

    b = a + "xyz"
    b.display()
    print(b)

    a.mul(3)
    print(a)






7.类的设计
--------------------



8.类的高级主题
----------------------