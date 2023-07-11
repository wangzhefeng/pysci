# -*- coding: utf-8 -*-


# *********************************************
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : 数学基础计算方法
# *               1.计算多个数字的最小公倍数
# *               2.计算多个数字的最大公约数
# *               3.
# * Link        : link
# **********************************************


# python libraries
import os
import sys


# global variable
GLOBAL_VARIABLE = None


def func():
    pass


class MathBasic:
    """
    数学基础类
    """
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def _getGreater(self) -> None:
        """
        获取最大的数
        """
        if self.x > self.y:
            self.greater = self.x
        else:
            self.greater = self.y

    def _getSmaller(self) -> None:
        """
        获取最小的数
        """
        if self.x > self.y:
            self.smaller = self.x
        else:
            self.smaller = self.y

    def getMaxCommonMultiple(self) -> int:
        """
        计算两个数的最大公倍数

        Returns:
            int: [description]
        """
        self._getGreater()
        while True:
            if (self.greater % self.x == 0) and (self.greater % self.y == 0):
                lcm = self.greater
                break
            self.greater += 1
        
        return lcm
        
    def getMinCommonDivisor(self) -> int:
        """
        计算两个数的最小公约数

        Raises:
            ValueError: [description]

        Returns:
            int: [description]
        """
        self._getSmaller()
        for i in range(1, self.smaller + 1):
            if ((self.x % i == 0) and (self.y % i == 0)):
                hcf = i
            else:
                raise ValueError(f"{self.x} and {self.y} have no minium common divisor.")

        return hcf


class MathSequence:

    def __init__(self) -> None:
        pass


# 测试代码 main 函数
def main():
    math_basic = MathBasic(21, 22)
    max_common_multiple = math_basic.getMaxCommonMultiple()
    print(max_common_multiple)
    min_common_dividor = math_basic.getMinCommonDivisor()
    print(min_common_dividor)



if __name__ == "__main__":
    main()

