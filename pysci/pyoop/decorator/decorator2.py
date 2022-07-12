
"""
函数装饰器也可能用来处理函数属性, 并且类装饰器可能动态地插入新的类属性, 
或者甚至新的方法。考虑如下的函数装 饰器——它们把函数属性分配给记录信息, 
以便随后供一个 API 使用, 但是, 它们没有插入一个包含器层来拦截随后的调用.
"""

def decorate(func):
    func.marked = True
    return func


def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate


@decorate
def spam(a, b):
    return a + b
print(spam.marked)


@annotate("spam data")
def spam(a, b):
    return a + b
spam(1, 2)
print(spam.label)
