#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyBeautifuleGril(object):
    """
    我的漂亮女神
    """
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifuleGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + "，我一见钟情！")
            MyBeautifuleGril.__isFirstInit = True
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就是我心中的唯一！")


# ----------------------------------------------
# 测试代码
# ----------------------------------------------
def TestLove():
    jenny = MyBeautifuleGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifuleGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), "id(kimi)", id(kimi))

def main():
    TestLove()

if __name__ == "__main__":
    main()

