
# -*- coding: utf-8 -*-


import logging
logging.basicConfig(level = logging.INFO)


def func(num):
    """
    定义内部函数并返回
    """
    def firstInnerFunc():
        return "这是第一个内部函数"

    def secondInnerFunc():
        return "这是第二个内部函数"

    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc




def loggingDecorator(func):
    """
    记录日志的装饰器
    """
    def wrapperLogging(*args, **kwargs):
        logging.info("开始执行 %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 执行完成!" % func.__name__)
    return wrapperLogging

@loggingDecorator
def showInfo(*args, **kwargs):
    logging.info("这是一个测试函数, 参数: %s", (args, kwargs))

@loggingDecorator
def showMin(a, b):
    logging.info("%d、%d 中最小值是: %d" % (a, b, a + b))



class ClassDecorator:
    """类装饰器, 记录一个类被实例化的次数"""
    def __init__(self, func):
        self.__numOfCall = 0
        self.__func = func
    
    def __call__(self, *args, **kwargs):
        self.__numOfCall += 1
        obj = self.__func(*args, **kwargs)
        print("创建 %s 的第 %d 个实例:%s" % (self.__func.__name__, self.__numOfCall, id(obj)))

        return obj

@ClassDecorator
class MyClass:

    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name









if __name__ == "__main__":
    # ---------------------
    # Python 函数的特殊功能
    # ---------------------
    print(func(1))
    print(func(2))
    print(func(1)())
    print(func(2)())

    # ---------------------
    # Python 函数装饰器
    # ---------------------
    # version 1
    # decoratedShowInfo = loggingDecorator(showInfo)
    # decoratedShowInfo("arg1", "arg2", kwarg1 = 1, kwarg2 = 2)
    # decoratedShowMin = loggingDecorator(showMin)
    # decoratedShowMin(2, 3)

    # version 2
    showInfo("arg1", "arg2", kwarg1 = 1, kwarg2 = 2)
    showMin(2, 3)

    # ---------------------
    # Python 类装饰器
    # ---------------------
    tony = MyClass("Tony")
    karry = MyClass("Karry")
    print(id(tony))
    print(id(karry))

