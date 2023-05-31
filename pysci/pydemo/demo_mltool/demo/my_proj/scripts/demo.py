# -*- coding: utf-8 -*-


"""
@author: wangzhefeng
@date: 20190130
"""


from dataImport.read_csv_excel import read_train_test
from dataExport.submission import submit




# =================================================================
# read train and test data
# =================================================================
train_path = "E:/DataScience/mltool/demo/my_proj/data/train.csv"
test_path = "E:/DataScience/mltool/demo/my_proj/data/test.csv"
targetName = ""
submission_path = "E:/DataScience/mltool/demo/my_proj/submission/"

reader = read_train_test(train_path, test_path, targetName)
train, train_Id = reader.read_train()
test, test_Id = reader.read_test()
data_union = reader.data_union(train, test)
train_target = reader.get_train_target(train)

# =================================================================
# 缺失值检测、异常值检测、
# =================================================================









# =================================================================
#
# =================================================================



# =================================================================
# prediction
# =================================================================
predicts = []


# =================================================================
# save the test prediction to submission file
# =================================================================
sub = submit(submission_path, test_Id, targetName, predicts)
sub.save()