# -*- coding: utf-8 -*-

"""
@author:
@date:
"""

from sklearn.model_selection import ParameterGrid


def parameters(param_grid):
    param_combine = ParameterGrid(param_grid)
    param_combine_list = list(param_combine)

    return param_combine, param_combine_list

