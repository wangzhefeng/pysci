# -*- coding: utf-8 -*-

# ***************************************************
# * File        : tree_model.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-13
# * Version     : 0.1.071310
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


def run_feature_importance(data, model_name = "xgboost"):
    # 数据集构造
    df_copy = data.copy()
    y = df_copy["manner"].apply(lambda x: 1 if x == "AI" else 0)
    X = df_copy.drop([
        "manner", 
        "blast_furnace"
    ], axis = 1)
    
    # 数据集分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    # 模型构建
    fig, ax = plt.subplots(figsize = (10, 10))
    if model_name == "xgboost":
        model = XGBClassifier(n_estimators=100, random_state=42)
        # 模型拟合
        model.fit(X_train, y_train)
        """
        # 模型预测(测试集)
        preds = model.predict(X_test)
        y_pred = [int(value) for value in preds]
        
        # 模型评估
        accuracy = accuracy_score(y_test, y_pred)
        print(f"{'=' * 7}\nReport:\n{'=' * 7}\n{classification_report(y_test, y_pred)}")
        """
        # 特征重要性
        # print(f"{'=' * 19}\nFeature Importance:\n{'=' * 19}\n")
        plot_importance(model, ax = ax, max_num_features=50, importance_type='gain', height = 0.5)
        plt.show();
    elif model_name == "rfc":
        model = RandomForestClassifier(n_estimators=100, random_state = 42)
        # 模型拟合
        model.fit(X_train, y_train)
        """
        # 模型预测(测试集)
        preds = model.predict(X_test)
        y_pred = [int(value) for value in preds]
        
        # 模型评估
        accuracy = accuracy_score(y_test, y_pred)
        print(f"{'=' * 7}\nReport:\n{'=' * 7}\n{classification_report(y_test, y_pred)}")
        """
        # 特征重要性
        # print(f"{'=' * 19}\nFeature Importance:\n{'=' * 19}\n")
        plot_rfc_importance(model, ax = ax, X_train = X_train)
        plt.show();


def plot_rfc_importance(model, ax, X_train):
    # 特征重要性
    importances = model.feature_importances_
    # 特征重要性排序
    indices = np.argsort(importances)[::-1]
    # 特征标签
    feat_label = [X_train.columns[i] for i in indices]
    
    df = pd.DataFrame(
        {
            "importances": importances,
            "feat_label": feat_label,
        }
    )
    df = df.sort_values(by = "importances", ascending = False)
    sns.barplot(data = df, x = "importances", y = "feat_label")
    



# 测试代码 main 函数
def main():
    df = pd.DataFrame({
        "a1": ["1", "2", "2", "1"],
        "a2": [0, 1, 0, 1],
        "a": [1.1, 1.2, 1.3, 1.4],
    })
    df = df.set_index(["a1", "a2"])
    df.reset_index(inplace = True)
    df["manner"] = df["a1"].map(lambda x: "ma" if x == "1" else "ai")
    print(df)

if __name__ == "__main__":
    main()
