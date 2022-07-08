#!/usr/bin/env Python
# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod
# 引入 ABCMeta 和 abstractmethod


"""
- 将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和回复功能。
- 想点餐的订单一样，发送者(客户)与接收者(厨师)没有任何依赖关系，我们只要发送订单就能完成想要完成的任务，这在程序中叫做命令模式。
- 命令模式的最大特点是将具体的命令与对应的接收者相关联（捆绑），使得调用方不用关心具体的行动执行者及如何执行，只要发送正确的命令，就能准确无误地完成相应的任务。 就像军队，将军一声令下，士兵就得分秒不差，准确执行。
- 命令模式是一种高内聚的模式，之所以说是高内聚的是因为它把命令封装成对象，并与连接着关联在一起，从而使（命令的）请求者(Invoker)和接收者(Receiver)分离。
"""


class Chef():
    """厨师"""

    def steamFood(self, originalMaterial):
        print("%s 清蒸中..." %  originalMaterial)

        return "清蒸" + originalMaterial

    def stirFriedFood(self, originalMaterial):
        print("%s 爆炒中..." % originalMaterial)

        return "香辣炒" + originalMaterial


class Order(metaclass = ABCMeta):
    """订单"""

    def __init__(self, name, originalMaterial):
        self._chef = Chef()
        self._name = name
        self._originalMaterial = originalMaterial

    def getDisplayName(self):

        return self._name + self._originalMaterial

    @abstractmethod
    def processingOrder(self):
        pass


class SteamedOrder(Order):
    """清蒸"""

    def __init__(self, originalMaterial):
        super().__init__("清蒸", originalMaterial)

    def processingOrder(self):
        if(self._chef is not None):
            return self._chef.steamFood(self._originalMaterial)
        
        return ""


class SpicyOrder(Order):
    """香辣炒"""

    def __init__(self, originalMaterial):
        super().__init__("香辣抄", originalMaterial)

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.stirFriedFood(self._originalMaterial)

        return  ""


class  Waiter:
    """服务员"""

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receiveOrder(self, order):
        self.__order = order
        print("服务员%s: 您的 %s 订单已经收到,请耐心等待" % (self.__name, order.getDisplayName()))

    def placeOrder(self):
        food = self.__order.processingOrder()
        print("服务员%s: 您的餐 %s 已经准备好了,请您慢用!" % (self.__name, food))


def testOrder():
    waiter = Waiter("Anna")
    steamedOrder = SteamedOrder("大闸蟹")
    print("客户 David: 我要一份 %s" % steamedOrder.getDisplayName())
    waiter.receiveOrder(steamedOrder)
    waiter.placeOrder()
    print()

    spicyOrder = SpicyOrder("大闸蟹")
    print("客户 Tony: 我要一份 %s" % spicyOrder.getDisplayName())
    waiter.receiveOrder(spicyOrder)
    waiter.placeOrder()

testOrder()

