# -*- coding: utf-8 -*-

# ***************************************************
# * File        : python_descriptor.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-21
# * Version     : 0.1.072121
# * Description : Python 描述符(descriptor):  一个实现了 描述符协议 的类就是一个描述符
# *               描述符给我们带来的编码上的便利, 它在实现 保护属性不受修改、属性类型检查 的基本功能, 同时有大大提高代码的复用率
# *               什么是描述符协议: 在类里实现了 __get__()、__set__()、__delete__() 其中至少一个方法: 
# *                  - __get__: 用于访问属性. 它返回属性的值, 若属性不存在、不合法等都可以抛出对应的异常
# *                  - __set__: 将在属性分配操作中调用. 不会返回任何内容
# *                  _ __delete__: 控制删除操作. 不会返回内容
# *               描述符分两种: 
# *                   - 数据描述符: 实现了__get__ 和 __set__ 两种方法的描述符
# *                   - 非数据描述符: 只实现了__get__ 一种方法的描述符
# *               数据描述器和非数据描述器的区别在于: 它们相对于实例的字典的优先级不同, 
# *               如果实例字典中有与描述符同名的属性, 如果描述符是数据描述符, 优先使用数据描述符, 
# *               如果是非数据描述符, 优先使用字典中的属性
# * Link        : https://mp.weixin.qq.com/s?__biz=Mzg3MjU3NzU1OA==&mid=2247496467&idx=1&sn=927f0093e62a78a1a04d1b0305c45c7a&source=41#wechat_redirect
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class Student:

    def __init__(self, name, math, chinese, english) -> None:
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english
    
    def __repr__(self):
        return f"<Student: {self.name}, math: {self.math}, chinese: {self.chinese}, english: {self.english}>"





# 测试代码 main 函数
def main():
    std1 = Student("xiaoming", 7, 8, 9)
    print(std1)

if __name__ == "__main__":
    main()
