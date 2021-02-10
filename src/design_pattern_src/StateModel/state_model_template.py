#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Context(metaclass = ABCMeta):
    """
    状态模式的上下文环境类
    """
    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0

    def addState(self, state):
        if (state not in self.__states):
            self.__states.append(state)

    def changeState(self, state):
        if (state is None):
            return False
        if (self.__curState is None):
            print("初始化为", state.getName())
        else:
            print("由", self.__curState.getName(), "变为", state.getName())

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if (state.isMatch(stateInfo)):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """
    状态的基类
    """
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        """
        状态的属性 stateInfo 是否在当前的状态范围内
        :param stateInfo:
        :return:
        """
        return False

    @abstractmethod
    def behavior(self, context):
        pass
