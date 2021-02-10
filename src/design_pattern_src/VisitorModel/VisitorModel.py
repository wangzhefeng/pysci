# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class DataNode(metaclass = ABCMeta):
    """数据结构类"""

    def accept(self, visitor):
        """接受访问者的访问"""
        visitor.visit(self)


class Visitor(metaclass = ABCMeta):
    """访问者"""

    @abstractmethod
    def visit(self, data):
        """
        对数据对象的访问操作
            Visitor的访问方法只有一个方法，是因为Python不支持方法的重载
        """
        pass


class ObjectStructure:
    """数据结构的管理类，也是数据对象的一个容器，可遍历容器的所有元素"""

    def __init__(self):
        self.__datas = []
    
    def add(self, dataElement):
        self.__datas.append(dataElement)
    
    def action(self, visitor):
        """进行数据访问的操作"""
        for data in self.__datas:
            data.accept(visitor)
