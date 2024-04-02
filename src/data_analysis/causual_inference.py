# -*- coding: utf-8 -*-

# ***************************************************
# * File        : causual_inference.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-07-14
# * Version     : 0.1.071410
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

import matplotlib.pyplot as plt
import dowhy
from dowhy import CausalModel
import dowhy.datasets
from IPython.display import Image, display

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]



# data
data = dowhy.datasets.linear_dataset(
    beta=10,  # beta 表示真实的因果效应
    num_common_causes=5,  # 混杂因子，用 W 表示，作用于干预变量和结果变量
    num_instruments=2,  # 工具变量，用 Z 表示，作用于干预变量(间接影响结果)
    num_effect_modifiers=1,  # 效果修改变量，用 X 表示，作用于结果变量
    num_samples=10000,  # 样本数量
    treatment_is_binary=True,  # 干预为二值变量，用 v 表示
    num_discrete_common_causes=1
)
df = data["df"]
print(df.head())


# model
model = CausalModel(
    data = df,
    treatment=data["treatment_name"],
    outcome=["outcome_name"],
    graph=data["gml_graph"],
)
model.view_model()
display(Image(filename="causal_model.png"))

# identify
identified_estimand = model.identify_effect()
print(identified_estimand)


# estimate
estimate = model.estimate_effect(
    identified_estimand, 
    method_name = "backdoor.propensity_score_stratification",
)
print(estimate)
print(f"Causal Estimate is {estimate.value}")




# 测试代码 main 函数
def main():
    pass

if __name__ == "__main__":
    main()
