
# -*- coding: utf-8 -*-

# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class WaterHeater:
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        self.__observes = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是：" + str(self.__temperature) + "℃")
        self.notifies()

    def addObserver(self, observer):
        self.__observes.append(observer)

    def notifies(self):
        for o in self.__observes:
            o.update(self)


class Observer(metaclass = ABCMeta):
    """洗澡模式和饮用模式的父类"""

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """该模式用于洗澡"""
    
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    """该模式用于饮用"""
    
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")




# -----------------------
# 测试代码
# -----------------------
def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


def main():
    testWaterHeater()


if __name__ == "__main__":
    main()