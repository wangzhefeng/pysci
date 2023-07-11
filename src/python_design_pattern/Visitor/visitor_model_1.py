# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from VisitorModel import DataNode, Visitor, ObjectStructure


"""
封装一些作用于某种数据结构中各元素的操作, 它可以在不改变数据结构的前提下定义作用于这些元素的新的操作. 

访问模式的核心思想在于: 
    - 可以在不改变数据结构的前提下定义作用于这些元素的新操作
    - 将数据结构和操作(或算法)进行解耦, 而且能更方便地拓展新的操作
"""


#TODO
class DesignPatternBook(DataNode):
    """
    《从生活的角度解读设计模式》一书
    """
    def getName(self):
        return "《从生活的角度解读设计模式》"


# class Reader(metaclass = ABCMeta):
#     """
#     访问者, 也就是读者
#     """
#     @abstractmethod
#     def visit(self, book):
#         pass


class Engineer(Visitor):
    """
    工程师
    """
    def visit(self, book):
        """[summary]

        :param book: DesignPatternBook 实例
        :type book: [type]
        """
        print("技术人读%s一书后的感受: 能抓住模式的核心思想, 深入浅出, 很有见地!" % book.getName())


class ProductManager(Visitor):
    """
    产品经理
    """
    def visit(self, book):
        """[summary]

        :param book: DesignPatternBook 实例
        :type book: [type]
        """
        print("产品经理%s一书后的感受: 配图非常有趣, 文章很有层次感!" % book.getName())


class OtherFriend(Visitor):
    """
    IT圈外的朋友
    """
    def visit(self, book):
        """[summary]

        :param book: DesignPatternBook 实例
        :type book: [type]
        """
        print("IT圈外的朋友读%s一书 后的感受: 技术的内容一脸懵, 但故事很精彩, 像看小说或故事集!" % book.getName())



def testBook():
    book = DesignPatternBook()
    fans = [
        Engineer(), 
        ProductManager(), 
        OtherFriend(),
    ]
    for fan in fans:
        fan.visit(book)


def testVisitBook():
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())


if __name__ == "__main__":
    print("testBook() result:")
    testBook()
    print()
    print("testVisitBook() result:")
    testVisitBook()
