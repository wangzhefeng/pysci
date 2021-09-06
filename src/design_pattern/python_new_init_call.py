# -*- coding: utf-8 -*-


"""
* __new__ 是一个类方法，而 __init__ 和 __call__ 是一个对象方法；
"""


class ClassA:

    def __new__(cls):
        """
        * __new__ 负责对象的创建；
            __new__ 是构造函数，负责对象的创建，它需要返回一个示例；
            __new__ 是通过类名进行实例化对象时自动调用的；
            __new__ 方法创建一个实例之后返回这个实例对象，
                    并将其传递给 __init__ 方法的 self 参数
        """
        print("ClassA.__new__")
        return super().__new__(cls)

    def __init__(self):
        """
        * __init__ 负责对象的初始化；
            __init__ 是在每一次实例化对象之后调用的；
            __init__ 是初始化函数，负责对 __new__ 实例化的对象进行初始化，
                     即负责对象状态的更新和属性的设置，因此它不允许有返回值。
            __init__ 方法中除了 self 定义的参数，其他参数都必须与 __new__
                     方法中除 cls 参数外的参数保持一致或者等效。
        """
        print("ClassA.__init__")

    def __call__(self, *args):
        """
        * __call__ 声明这个类的对象是可调用的(callable)；
            callable() 内建函数：判断一个对象是否可以调用；
            __call__ 的作用就是声明这个类的对象是可调用的(callable),
                     即实现 __call__ 方法之后，用 callable 调用这个
                     类的对象时，结果为 True
        """
        print("ClassA.__call__ args:", args)


a = ClassA()
a("arg1", "arg2")


"""
ClassA.__new__
ClassA.__init__
ClassA.__call__ args: ('arg1', 'arg2')
"""

