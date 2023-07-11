# -*- coding: utf-8 -*-


"""
submission file
"""


import os
import pandas as pd


class submit(object):

    def __init__(self, path, test_Id, targetName, predicts):
        self.path = path
        self.test_Id = test_Id
        self.targetName = targetName
        self.predicts = predicts

    def save(self):
        sub = pd.DataFrame()
        sub["ID"] = self.test_Id
        sub[str(self.targetName)] = self.predicts

        sub.to_csv(self.path, index = False)
