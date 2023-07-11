
class tracer:
    """
    统计被装饰函数的调用次数
    """
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)











if __name__ == "__main__":
    @tracer
    def spam(a, b, c):
        print(a + b + c)
    
    spam(1, 2, 3)
    spam(1, 2, 3)
    spam(1, 2, 3)
