#!/usr/bin/env python
# -*- coding utf-8 -*-


from scipy import integrate
import numpy as np


def fun(x):
    return x + 1

v, err = integrate.quad(fun, 1, 2)
print(v)
print(err)
