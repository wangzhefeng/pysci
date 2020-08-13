#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person_v1(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for key, value in kw.items():
            setattr(self, key, value)


class Person_v2(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        self.__dict__.update(kw)

p1 = Person_v1("wangzf", "male", age = 18, course = "Python")
p2 = Person_v2("wangzf", "male", age = 18, course = "Python")

print(p1.age)
print(p1.course)

print(p2.age)
print(p2.course)