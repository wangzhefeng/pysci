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


class Water(Context):
    """
    水(H2O)
    """
    def __init__(self):
        super().__init__()
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemprature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    """
    构造一个单例的装饰器
    :param cls:
    :param args:
    :param kwargs:
    :return:
    """
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState():
    """
    固态
    """
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("我性格高冷，当前体温", context._getStateInfo(), "℃，我坚如钢铁，彷如一冷血动物，请用我砸人，嘿嘿......")


@singleton
class LiquidState():
    """
    液态
    """
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)

    def behavior(self, context):
        print("我性格温和，当前体温", context._getStateInfo(), "℃，我可滋润万物，饮用我可让你活力倍增......")


@singleton
class GaseousState():
    """
    气态
    """
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("我性格热烈，当前体温", context._getStateInfo(), "℃，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到我的境界......")


# ------------------------------------
# 测试代码
# ------------------------------------
def testState():
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()


def main():
    testState()

if __name__ == "__main__":
    main()