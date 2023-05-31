# fib.py
import math

_SQRT_5 = math.sqrt(5)
_PHI = (1 + _SQRT_5) / 2


def approx_fib(n):
    """Approximate Fibonacci sequence

    :param n: The place in Fibonacci sequence to approximate
    :type n: int
    :return: The approximate value in Fibonacci sequence
    :rtype: float
    """
    return round(_PHI ** (n + 1) / _SQRT_5)

