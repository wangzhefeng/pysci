
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Observer(metaclass = ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""
    
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserber(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object = 0):
        for o in self.__observers:
            o.update(self, object)

