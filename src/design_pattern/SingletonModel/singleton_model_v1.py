
# -*- coding: utf-8 -*-


"""
单例模式就是保证一个类有且只有一个对象(实例)的一种机制。
单例模式用来控制某些事物只允许有一个个体，
比如，在我们生活的世界中，有生命的星球只有一个地球(至少目前为止在人类所探索到的世界中是这样的)。
"""



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

