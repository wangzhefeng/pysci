#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ----------------------------------------------
# type()
# type() 的两个主要的功能：
    # 1. 查看一个变量(对象)的类型
    # 2. 创建一个类(class)
# ----------------------------------------------
# 1. 查看一个变量(对象)的类型
class ClassA:
    name = "type test"

a = ClassA()
b = 3.0
c = "String"

print(type(a))
print(a.__class__)
print(type(b))
print(b.__class__)
print(type(c))
print(c.__class__)


# 2. 创建一个类(class)
ClassVarable = type("ClassA",
                    (object,),
                    dict(name = "type test"))
a = ClassVarable()
print(type(a))
print(a.name)


# ----------------------------------------------
# isinstance()
# isinstance() 的作用是判断一个对象是不是某个类型的实例
# isinstance(object, classinfo)
# ----------------------------------------------
class BaseClass:
    name = "Base"

class SubClass(BaseClass):
    pass

base = BaseClass()
sub = SubClass()
print(isinstance(base, BaseClass))
print(isinstance(base, SubClass))
print(isinstance(sub, SubClass))
print(isinstance(sub, BaseClass))


# ----------------------------------------------
# issubclass()
# 要知道子类与父类之间的继承关系，可用
# * issubclass() 方法
# * object.__bases__ 方法
# ----------------------------------------------
class BaseClass:
    name = "Base"

class SubClass(BaseClass):
    pass

print(issubclass(SubClass, BaseClass))
print(issubclass(BaseClass, SubClass))
print(SubClass.__bases__)


