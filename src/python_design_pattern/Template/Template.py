from abc import ABC, ABCMeta, abstractmethod
# 引用 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法


"""
1. 对一些复杂的算法进行分割, 将其算法中固定不变的部分设计为模板方法和父类具体方法, 
   而一些可以改变的细节由其子类来实现. 即一次性实现一个算法的不变部分, 并将可变的行为留给子类来实现
2. 各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复
3. 需要通过子类来决定父类算法中某个步骤是否执行, 实现子类对父类的反向控制
"""


class Template(metaclass = ABCMeta):
    """
    模板类(抽象类)
    """

    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethod(self):
        """
        模板方法
        """
        self.stepOne()
        self.stepTwo()
        self.stepThree()


class TemplateImpA(Template):
    """
    模板实现类 A
    """
    def stepOne(self):
        print("步骤一")

    def stepTwo(self):
        print("步骤二")

    def stepThree(self):
        print("步骤三")


class TemplateImpB(Template):
    """
    模板实现类 B
    """
    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")
