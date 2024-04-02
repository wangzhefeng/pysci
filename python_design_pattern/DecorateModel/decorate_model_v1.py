
# -*- coding: utf-8 -*-


# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


class Person(metaclass = ABCMeta):
    """
    人
    """

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装: ")


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
        print("我是" + self.getSkill() + "工程师" + self._name, end = ", ")
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
        print("我是" + self._name + self.getTitle(), end = ", ")
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
    皮鞋装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一双深色的休闲皮鞋")


class KnittedSweaterDecorator(ClothingDecorator):
    """
    针织毛衣装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("意见紫红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    """
    白色衬衫装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件白色衬衣")


class GlassesDecorator(ClothingDecorator):
    """
    眼镜装饰器
    """
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一副方形黑色框眼镜")



# 测试代码
def testDecorator():
    tony = Engineer("Tony", "客户端")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorateTeacher = GlassesDecorator(
        WhiteShirtDecorator(
            LeatherShoesDecorator(
                Teacher("wells", "教授")
            )
        )
    )
    decorateTeacher.wear()


if __name__ == "__main__":
    testDecorator()


