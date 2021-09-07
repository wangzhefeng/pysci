# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from VisitorModel import DataNode, Visitor, ObjectStructure


class Animal(DataNode):
    """
    动物类
    """
    def __init__(self, name, isMale, age, weight):
        self.__name = name
        self.__isMale = isMale
        self.__age = age
        self.__weight = weight
    
    def getName(self):
        return self.__name

    def isMale(self):
        return self.__isMale
    
    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight


class Cat(Animal):
    """
    猫
    """
    def __init__(self, name, isMale, age, weight):
        super().__init__(name, isMale, age, weight)
    
    def speak(self):
        print("miao~")


class Dog(Animal):
    """
    狗
    """
    def __init__(self, name, isMale, age, weight):
        super().__init__(name, isMale, age, weight)
    
    def speak(self):
        print("wang~")


class GenderCounter(Visitor):
    """
    性别统计
    """
    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femaleDog = 0

    def visit(self, data):
        """[summary]
        :param data: TODO
        :type data: [type]
        """
        if isinstance(data, Cat):
            if data.isMale():
                self.__maleCat += 1
            else:
                self.__femaleCat += 1
        elif isinstance(data, Dog):
            if data.isMale():
                self.__maleDog += 1
            else:
                self.__femaleDog += 1
        else:
            print("Not support this type")

    def getInfo(self):
        print(f"{self.__maleCat} 只雄猫，{self.__femaleCat} 只雌猫，{self.__maleDog} 只雄狗，{self.__femaleDog} 只雌狗.")


class WeightCounter(Visitor):
    """
    体重统计
    """
    def __init__(self):
        self.__catNum = 0
        self.__catWeight = 0
        self.__dogNum = 0
        self.__dogWeight = 0

    def visit(self, data):
        """[summary]
        :param data: TODO
        :type data: [type]
        """
        if isinstance(data, Cat):
            self.__catNum += 1
            self.__catWeight += data.getWeight()
        elif isinstance(data, Dog):
            self.__dogNum += 1
            self.__dogWeight += data.getWeight()
        else:
            print("Not support this type.")
    
    def getInfo(self):
        print("猫的平均体重是: %0.2fkg, 狗的平均体重是: %0.2fkg" % (self.__catWeight / self.__catNum, self.__dogWeight / self.__dogNum))


class AgeCounter(Visitor):
    """
    年龄统计
    """
    def __init__(self):
        self.__catMaxAge = 0
        self.__dogMaxAge = 0
    
    def visit(self, data):
        if isinstance(data, Cat):
            if self.__catMaxAge < data.getAge():
                self.__catMaxAge = data.getAge()
        elif isinstance(data, Dog):
            if self.__dogMaxAge < data.getAge():
                self.__dogMaxAge = data.getAge()
        else:
            print("Not support this type.")

    def getInfo(self):
        print("猫的最大年龄是: %s, 狗的最大年龄是: %s" % (self.__catMaxAge, self.__dogMaxAge))



def testAnimal():
    animals = ObjectStructure()
    animals.add(Cat("Cat1", True, 1, 5))
    animals.add(Cat("Cat2", False, 0.5, 3))
    animals.add(Cat("Cat3", True, 1.2, 4.2))
    animals.add(Dog("Dog1", True, 0.5, 8))
    animals.add(Dog("Dog2", True, 3, 52))
    animals.add(Dog("Dog3", False, 1, 21))
    animals.add(Dog("Dog4", False, 2, 25))
    # 性别统计
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()
    # 体重统计
    weightCounter = WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()
    print()
    # 年龄统计
    ageCounter = AgeCounter()
    animals.action(ageCounter)
    ageCounter.getInfo()


if __name__ == "__main__":
    testAnimal()
