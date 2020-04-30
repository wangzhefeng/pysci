
## Python 类和对象

> 



## `__repr__()` 和 `__str()`

> 重新定义实例的 `__repr__()` 和 `__str__()` 方法可以 改变对象实例的打印或显示输出，让它们更具可读性
> `__repr__()` 方法返回一个实例的代码表示形式，通常用来重新构造这个实例，内置的 `repr()` 函数返回这个字符串，跟使用交互式解释器显示的值是一样的
> `__str__()` 方法将实例转换为一个字符串，使用 `str()` 或 `print()` 函数会输出这个字符串

```python
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Pair({0.x!r}, {0.y!r})".format(self) 
        # "Pair({%r}, {%r})".format(self.x, self.y)
    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)
        # "Pair({%s}, {%s})".format(self.x, self.y)

>>> p = Pair(3, 4)
>>> p
>>> # Pair(3, 4)
>>> print(p)
>>> # (3, 4)
```


## `__format__()`