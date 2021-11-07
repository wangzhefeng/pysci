# -*- coding: utf-8 -*-


import os
import pandas as pd


class read_train_test(object):

    def __init__(self, trainPath, testPath, targetName):
        self.trainPath = trainPath
        self.testPath = testPath
        self.targetName = targetName

    def read_train(self):
        train = pd.read_csv(self.trainPath)
        train_Id = train["Id"]
        train.drop("Id", axis = 1, inplace = True)

        return train, train_Id

    def read_test(self):
        test = pd.read_csv(self.testPath)
        test_Id = test["Id"]
        test.drop("Id", axis = 1, inplace = True)

        return test, test_Id

    def data_union(self, train, test):
        data_union = pd.concat((train, test)).reset_index(drop = True)
        data_union.drop([self.targetName], axis = 1, inplace = True)

        return data_union

    def get_train_target(self, train):
        targetName = self.targetName
        train_target = train[targetName].values

        return train_target

    def model_data(self, data_union, train_target):
        x_train = data_union[:train_target.shape[0]]
        x_test = data_union[train_target.shape[0]:]
        y = train_target

        return x_train, x_test, y
