# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from VisitorModel import DataNode, Visitor, ObjectStructure


class Animal(DataNode):
    """动物类"""

    def __init__(self, name, isMale, age, weight):
        self.__name = name
        self.isMale = isMale
        self.__age = age
        self.__weight = weight
    
    def getName(self):

        return self.__name

    def isMale(self):

        return self.isMale
    
    def getAge(self):

        return self.__age

    def getWeight(self):

        return self.__weight
    
class Cat(Animal):
    """猫"""
    
    def __init__(self, name, isMale, age, weight):
        super.__init__(name, isMale, age, weight)
    
    def speak(self):
        print("miao~")
    
class Dog(Animal):
    """狗"""

    def __init__(self, name, isMale, age, weight):
        super.__init__(name, isMale, age, weight)
    
    def speak(self):
        print("wang~")
    
class GenderCounter(Visitor):
    """性别统计"""

    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femaleDog = 0


class WeightCounter(Visitor):
    pass

class AgeCounter(Visitor):
    pass





def testAnimal():
    animals = ObjectStructure()
    animals.add(Cat("Cat1", True, 1, 5))
    animals.add(Cat("Cat2", False, 0.5, 3))
    animals.add(Cat("Cat3", True, 1.2, 4.2))
    animals.add(Cat("Dog1", True, 0.5, 8))
    animals.add(Cat("Dog2", True, 3, 52))
    animals.add(Cat("Dog3", False, 1, 21))
    animals.add(Cat("Dog4", False, 2, 25))
    
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()

    weightCounter = WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()
    print()

    ageCounter = AgeCounter()
    animals.action(ageCounter)
    ageCounter.getInfo()

