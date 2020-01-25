#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Person(metaclass = ABCMeta):
    """
    人
    """
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    """
    工程师
    """
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是" + self.getSkill() + "工程师" + self._name, end = "，")
        super().wear()


class Teacher(Person):
    """
    教师
    """
    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("我是" + self._name + self.getTitle(), end = "，")
        super().wear()


class ClothingDecorator(Person):
    """
    服饰装饰器的基类
    """
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """
    休闲裤装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条卡其色休闲裤")


class BeltDecorator(ClothingDecorator):
    """
    腰带装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条银色针扣头的黑色腰带")


class LeatherShoesDecorator(ClothingDecorator):
    """

    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一双深色的休闲皮鞋")


class KnittedSweaterDecorator(ClothingDecorator):
    """

    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("意见紫红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    """

    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件白色衬衣")


class GlassesDecorator(ClothingDecorator):
    """

    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一副方形黑色框眼镜")









