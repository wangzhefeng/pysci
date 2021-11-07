# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# **********************************************


# python libraries
import os
import sys
import time
import functools


# **********************************************
# * 1.装饰器基础
# **********************************************
def foo_v1():
    """
    需求: 想看看执行这个函数用了多长时间
    """
    print("in foo")


def foo_v2():
    """
    需求: 想看看执行这个函数用了多长时间
    """
    start = time.time()
    print("in foo_v2")
    end = time.time()
    print(f"used: {end - start}")


def timeit_v1(func):
    """
    计时函数
    Args:
        func ([type]): [description]
    """
    start = time.time()
    func()
    end = time.time()
    print(f"used: {end - start}")


def timeit_v2(func):
    """
    定义一个计时器，传入一个函数，并返回另一个附加了计时功能的方法

    Args:
        func ([type]): [description]
    """
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"used: {end - start}")
    
    # 将包装后的函数返回
    return wrapper


@timeit_v2
def foo_v3():
    print("in foo_v3")


def test_1():
    foo_v3()
    print(f"foo_v3.__name__: {foo_v3.__name__}")

# **********************************************
# * 2.内置装饰器
# **********************************************
class Rabbit:
    """
    内置装饰器有三个：
        1.staticmethod: 把类中定义的实例方法变成静态方法
        2.classmethod: 把类中定义的实例方法变成类方法
        3.property: 把类中定义的实例方法变成类属性
    由于模块里可以定义函数，所以静态方法和类方法的用处并不是太多，除非你想要完全的面向对象编程
    """
    def __init__(self, name: str) -> None:
        self._name = name

    @staticmethod
    def newRabbit(name):
        """
        静态方法

        Args:
            name ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Rabbit()

    @classmethod
    def newRabbit2(cls):
        """
        类方法

        Returns:
            [type]: [description]
        """
        return Rabbit("")

    @property
    def name(self):
        """
        只读类属性

        Returns:
            [type]: [description]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        可写属性

        Args:
            name ([type]): [description]
        """
        self._name = name


def test_2():
    pass

# **********************************************
# * 3.functools 模块
# **********************************************
def timeit_v3(func):
    """
    functools 模块提供了两个装饰    
    wraps 装饰器：
        1.函数有几个特殊属性比如函数名，在被装饰后，函数名会变成包装函数的名字 wrapper
        2.如果希望使用反射，可能会导致意外的结果，这个装饰器可以解决这个问题，它能将装饰过的函数的特殊属性保留

    Args:
        func ([type]): [description]
    """
    @functools.wraps(func)
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"used: {end - start}")
    
    return wrapper


@timeit_v3
def foo_v4():
    print("in foo_v4")


def total_ordering(cls):
    """
    functools.total_ordering 装饰器的源码
    它的作用是为了实现了至少 __it__, __le__, __gt__, __ge__ 其中一个的类加上其他的比较方法，这是一个类装饰器
    Class decorator that fills in missing ordering methods
    """
    convert = {
        '__lt__': [
            ('__gt__', lambda self, other: other < self),
            ('__le__', lambda self, other: not other < self),
            ('__ge__', lambda self, other: not self < other)
        ],
        '__le__': [
            ('__ge__', lambda self, other: other <= self),
            ('__lt__', lambda self, other: not other <= self),
            ('__gt__', lambda self, other: not self <= other)
        ],
        '__gt__': [
            ('__lt__', lambda self, other: other > self),
            ('__ge__', lambda self, other: not other > self),
            ('__le__', lambda self, other: not self > other)
        ],
        '__ge__': [
            ('__le__', lambda self, other: other >= self),
            ('__gt__', lambda self, other: not other >= self),
            ('__lt__', lambda self, other: not self >= other)
        ]
    }
    roots = set(dir(cls)) & set(convert)
    if not roots:
        raise ValueError('must define at least one ordering operation: < > <= >=')
    root = max(roots)       # prefer __lt__ to __le__ to __gt__ to __ge__
    for opname, opfunc in convert[root]:
        if opname not in roots:
            opfunc.__name__ = opname
            opfunc.__doc__ = getattr(int, opname).__doc__
            setattr(cls, opname, opfunc)
    return cls


def test_3():
    foo_v4()
    print(f"foo_v4.__name__: {foo_v4.__name__}")




# 测试代码 main 函数
def main():
    test_1()
    test_2()
    test_3()



if __name__ == "__main__":
    main()

