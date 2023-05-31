# -*- coding: utf-8 -*-

"""
@author:
@date:
"""

import os
from sklearn.externals import joblib


class model_save(object):

    def __init__(self, path, model):
        self.path = path
        self.model = model

    def save(self):
        joblib.dump(self.model, self.path)

    def load(self):
        model = joblib.load(self.path)

        return model
