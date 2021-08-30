
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


def rangetest(*argchecks):      # Validate positional arg ranges
    def onDecorator(func):
        if not __debug__:       # Ture, if "python -O main.py args..."
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = "Argument %s not in %s..%s" % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator









if __name__ == "__main__":
    @tracer
    def spam(a, b, c):
        print(a + b + c)
    
    spam(1, 2, 3)
    spam(1, 2, 3)
    spam(1, 2, 3)
