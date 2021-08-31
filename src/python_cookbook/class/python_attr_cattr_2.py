# -*- coding: utf-8 -*-# class 3


from attr import attrs, attrib, fields, validators
from cattr import structure, unstructure


# class 1
@attrs
class Point(object):
    x = attrib()
    y = attrib()


# class 2
def is_valid_gender(instance, attribute, value):
    if value not in ["male", "female"]:
        raise ValueError(f"gender {value} is not vaild.")

@attrs
class Person(object):
    name = attrib()
    gender = attrib(validator = is_valid_gender)
    age = attrib(validator = validators.instance_of(int))


if __name__ == "__main__":
    # 声明和比较
    p1 = Point(x = 1, y = 2)
    p2 = Point(x = 1, y =2)
    print(p1)
    print(p2)
    print('Equal(eq):', Point(1, 2) == Point(1, 2))
    print('Not Equal(ne):', Point(1, 2) != Point(3, 4))
    print('Less Than(lt):', Point(1, 2) < Point(3, 4))
    print('Less or Equal(le):', Point(1, 2) <= Point(1, 4), Point(1, 2) <= Point(1, 2))
    print('Greater Than(gt):', Point(4, 2) > Point(3, 2), Point(4, 2) > Point(3, 1))
    print('Greater or Equal(ge):', Point(4, 2) >= Point(4, 1))
    # 属性定义
    print(fields(Point))
    # 属性名 `x = attrib()`
    # 默认值 `default = 100`
    # 初始化 `init = False`
    # 强制关键字 `kw_only = True`
    # 验证器
    print(Person(name = "Mike", gender = "male", age = "18"))
    print(Person(name = "Mike", gender = "mlae", age = 20))
    # 转换器
    # 类型
    # 序列转换
    # 基本转换
    # 多类型转换
    # 属性处理
    # 嵌套处理