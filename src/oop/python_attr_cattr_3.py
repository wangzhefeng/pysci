# -*- coding: utf-8 -*-


# class 3
from attr import attrs, attrib, fields, validators
from cattr import structure, unstructure
from typing import List

@attrs
class Point(object):
    x = attrib(type = int, default = 0)
    y = attrib(type = int, default = 0)

@attrs
class Color(object):
    r = attrib(default = 0)
    g = attrib(default = 0)
    b = attrib(default = 0)

@attrs
class Line(object):
    color = attrib(type = Color)
    points = attrib(type = List[Point])


if __name__ == "__main__":
    point = Point(x = 1, y = 2)
    # 基本转换
    json = unstructure(point)
    print("json:", json)
    obj = structure(json, Point)
    print("obj:", obj)
    # 多类型转换







