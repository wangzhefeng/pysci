# -*- coding: utf-8 -*-


import attr
from attr import s, attributes, attrs
from attr import ib, attr, attrib
from attr import fields, validators, Factory
import cattr
from cattr import structure, unstructure
import typing


# ==========================================
# 基本用法
# ==========================================
class Color_1(object):
    """
    Color Object of RGB
    R: 0-255
    G: 0-255
    B: 0-255
    RGB(r, g, b)
    """
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __repr__(self):
        """
        在 Python 里面想要定义某个对象本身的打印输出结果的时候，需要实现它 __repr__ 方法
        """
        return f"{self.__class__.__name__}(r={self.r}, g={self.g}, b={self.b})"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__): 
            return NotImplemented
        
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__): 
            return NotImplemented
        
        return (self.r, self.g, self.b) < (other.r, other.g, other.b)

    def __gt__(self, other):
        if not isinstance(other, self.__class__): 
            return NotImplemented
        
        return (self.r, self.g, self.b) > (other.r, other.g, other.b)
    
    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return (self.r, self.g, self.b) <= (other.r, other.g, other.b)
    
    def __ge__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return (self.r, self.g, self.b) >= (other.r, other.g, other.b)
    
    def __hash__(self):
        return hash((self.__class__, self.r, self.g, self.b))


@attrs
class Color_2(object):
    """
    Color Object of RGB
    R: 0-255
    G: 0-255
    B: 0-255
    RGB(r, g, b)
    """
    r = attrib(type = int, default = 0)
    g = attrib(type = int, default = 0)
    b = attrib(type = int, default = 0)


def test_color():
    color_1 = Color_1(255, 255, 255)
    print(color_1)

    color = Color_2(255, 255, 255)
    print(color)


# ==========================================
# 声明和比较
# ==========================================
@attrs
class Point_1(object):
    """
    Point 数据结构，包含 x, y 的坐标
    """
    x = attrib()
    y = attrib()


@attrs
class Point_2(object):
    """
    默认值
    """
    x = attrib()
    y = attrib(default = 100)


@attrs
class Point_3(object):
    """
    设置一个初始值，一直固定不变
    """
    x = attrib(init = False, default = 10)
    y = attrib(default = 100)


@attrs
class Point_4(object):
    """
    强制关键字
    """
    x = attrib(default = 0)
    y = attrib(kw_only = True)


def to_int(value):
    """
    整数类型转换器

    Args:
        value ([type]): 属性值

    Returns:
        [type]: [description]
    """
    try:
        return int(value)
    except:
        return None

@attrs
class Point_5(object):
    """
    转换器
    """
    x = attrib(converter = to_int)
    y = attrib()


@attrs
class Point_6(object):
    """
    类型-原生类型
    """
    x = attrib(type = int)
    y = attrib()


@attrs
class Point_7(object):
    """
    类型-typing 类型、attr 类型
    """
    x = attrib(type = int)
    y = attrib(type = typing.List[int])
    z = attrib(type = attr.Factory(list))


@attrs
class Line(object):
    """
    类型-类型嵌套
    """
    name = attrib()
    points = attrib(type = typing.List[Point_7])


def is_valid_gender(instance, attribute, value):
    """
    性别验证器方法

    Args:
        instance ([type]): 类对象
        attribute ([type]): 类属性
        value ([type]): 属性名

    Raises:
        ValueError: [description]
    """
    if value not in ["male", "female"]:
        raise ValueError(f"gender {value} is not vaild.")

def is_less_than_100(instance, attribute, value):
    """
    年龄验证器

    Args:
        instance ([type]): 类对象
        attribute ([type]): 类属性
        value ([type]): 属性名

    Raises:
        ValueError: [description]
    """
    if value > 100:
        raise ValueError(f"age {value} must less than 100")

@attrs
class Person(object):
    """
    验证器
    """
    name = attrib()
    gender = attrib(validator = is_valid_gender)
    age = attrib(validator = [validators.instance_of(int), is_less_than_100])


def test_point():
    print("# 声明和比较:")
    p1 = Point_1(1, 2)
    print(p1)
    p2 = Point_1(x = 1, y = 2)
    print(p2)
    print('Equal:', Point_1(1, 2) == Point_1(1, 2))
    print('Not Equal(ne):', Point_1(1, 2) != Point_1(3, 4))
    print('Less Than(lt):', Point_1(1, 2) < Point_1(3, 4))
    print('Less or Equal(le):', Point_1(1, 2) <= Point_1(1, 4), Point_1(1, 2) <= Point_1(1, 2))
    print('Greater Than(gt):', Point_1(4, 2) > Point_1(3, 2), Point_1(4, 2) > Point_1(3, 1))
    print('Greater or Equal(ge):', Point_1(4, 2) >= Point_1(4, 1))
    print("# 属性定义:")
    print(fields(Point_1()))
    print(Point_2(x = 1))  # 默认值
    print(Point_3(x = 10, y = 3))  # 初始化
    print(Point_4(1, y = 3))  # 强制关键字


def test_person():
    print(Person(name = "Mike", gender = "male", age = 10))
    print(Person(name = "Mike", gender = "mlae", age = 500))


# ==========================================
# 序列转换
# ==========================================
@attrs
class Point(object):
    x = attrib(type = int, default = 0)
    y = attrib(type = int, default = 0)







def test_convert():
    point = Point(x = 1, y = 2)
    json_data = cattr.unstructure(point)
    print(f"json: {json_data}")
    obj_data = cattr.structure(json_data, Point)
    print(f"obj: {obj_data}")








def main():
    pass


if __name__ == "__main__":
    main()

