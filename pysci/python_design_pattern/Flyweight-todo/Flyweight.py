import logging


class Pigment:
    """
    颜料
    """
    def __init__(self, color):
        self.__color = color
        self.__user = ""

    def getColor(self):
        return self.__color

    def setUser(self, user):
        self.__user = user
        return self

    def showInfo(self):
        print(f"{self.__user} 取得 {self.__color} 色颜料.")


class PigmentFactory:
    """
    颜料的工厂类
    """
    def __init__(self):
        self.__sigmentSet = {
            "红": Pigment("红"),
            "黄": Pigment("黄"),
            "蓝": Pigment("蓝"),
            "绿": Pigment("绿"),
            "紫": Pigment("紫"),
        }
    
    def getPigment(self, color):
        pigment = self.__sigmentSet.get(color)
        if pigment is None:
            logging.error(f"没有 {color} 颜色的颜料！")
        return pigment

def testPigment():
    factory = PigmentFactory()
    pigmentRed = factory.getPigment("红").setUser("梦之队")
    pigmentRed.showInfo()


if __name__ == "__main__":
    testPigment()
