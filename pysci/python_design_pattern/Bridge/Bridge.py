from abc import ABC, ABCMeta, abstractmethod
# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


"""
1. 一个产品（或对象）有多种分类和多种组合，即两个（或多个）独立变化的维度，
   每个维度都希望独立进行扩展
2. 因为使用继承或因为多层继承导致系统类的个数急剧增加的系统，可以改用桥接模式来实现
"""


class Shape(metaclass = ABCMeta):
    """
    形状
    """
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return self._color.getColor() + "的" + self.getShapeType()


class Rectange(Shape):
    """
    矩形
    """
    def __init__(self, color):
        super().__init__(color)
    
    def getShapeType(self):
        return "矩形"


class Ellipse(Shape):
    """
    椭圆
    """
    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "椭圆"



class Color(metaclass = ABCMeta):
    """
    颜色
    """
    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    """
    红色
    """
    def getColor(self):
        return "红色"


class Green(Color):
    """
    绿色
    """
    def getColor(self):
        return "绿色"



def testShape():
    redColor = Red()
    greenColor = Green()

    redRect = Rectange(redColor)
    print(redRect.getShapeInfo())

    greenRect = Rectange(greenColor)
    print(greenRect.getShapeInfo())

    redEllipse = Ellipse(redColor)
    print(redEllipse.getShapeInfo())

    greenEllipse = Ellipse(greenColor)
    print(greenEllipse.getShapeInfo())


if __name__ == "__main__":
    testShape()
