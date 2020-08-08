#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from attr import s, attributes, attrs
from attr import ib, attr, attrib
import cattr


# ==========================================
# class method 1
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


# ==========================================
# class method 2
# ==========================================
@attrs
class Color_2(object):
    r = attrib(type = int, default = 0)
    g = attrib(type = int, default = 0)
    b = attrib(type = int, default = 0)


if __name__ == "__main__":
    color_1 = Color_1(255, 255, 255)
    print(color_1)

    color = Color_2(255, 255, 255)
    print(color)

