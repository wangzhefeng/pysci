# -*- coding: utf-8 -*-

# ***************************************************
# * File        : pid.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2023-06-07
# * Version     : 0.1.060722
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
import time

import matplotlib.pyplot as plt
import numpy as np
# from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline


# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class PID:
    
    def __init__(self, P, I, D) -> None:
        # PID 系数
        self.Kp = P
        self.Ki = I
        self.Kd = D
        # 时间变量
        self.sample_time = 0.0  #TODO
        self.current_time = time.time()  # 当前时刻时间戳
        self.last_time = self.current_time  # 上次算法更新时刻时间戳
        # 重置
        self.clear()
    
    def clear(self):
        self.setpoint = 0.0  # 设定目标值
        self.P_term = 0.0  # P
        self.I_term = 0.0  # I
        self.D_term = 0.0  # D
        self.last_error = 0.0  # 上一时刻的误差
        self.output = 0.0  # 输出
    
    def update(self, feedback_value):
        # 时间差
        self.current_time = time.time()  # 当前时间
        delta_time = self.current_time - self.last_time

        # 误差差分
        error = self.setpoint - feedback_value  # 当前时刻误差
        delta_error = error - self.last_error
        
        # PID
        if delta_time >= self.sample_time:
            # PID 各项计算
            self.P_term = self.Kp * error  # 比例项
            self.I_term += error * delta_time  # 积分项
            self.D_term = delta_error / delta_time if delta_time > 0.0 else 0.0  # 微分项

            # 更新 last_time
            self.last_time = self.current_time
            # 更新 last error
            self.last_error = error
            # 更新输出
            self.output = self.P_term + (self.Ki * self.I_term) + (self.Kd * self.D_term)
        
    def set_sample_time(self, sample_time):
        self.sample_time = sample_time
 
    @staticmethod
    def visual(time_list, feedback_list, setpoint_list, END):
        print(f"time_list: {time_list}")
        print(f"setpoint_list: {setpoint_list}")
        fig = plt.figure()
        time_smooth = np.linspace(min(time_list), max(time_list), 300)
        print(f"time_smooth: {time_smooth}")
        feedback_smooth = make_interp_spline(time_list, feedback_list)(time_smooth)
        print(f"feedback_smooth: {feedback_smooth}")
        plt.plot(time_list, setpoint_list, 'r')  # 绘制设定目标曲线
        plt.plot(time_smooth, feedback_smooth, 'b-')  # 设定
        plt.xlim((0, END))
        plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))
        plt.xlabel('time (s)')
        plt.ylabel('PID (PV)')
        plt.title('PID test', fontsize = 15)
        plt.grid(True)
        plt.show()


def test_pid(P, I , D, END):
    # 实例化 PID 类
    pid = PID(P, I, D)
    
    # 设置参数
    pid.setpoint = 1.1  # 设置目标值
    pid.set_sample_time(sample_time = 0.01)  # 设置采样间隔时间
    time_list = list(range(1, END))
    feedback = 0.5  # 设置初始反馈值
    
    feedback_list = []  # 反馈值
    setpoint_list = []  # 设定值
    for i in time_list:
        # PID 更新
        pid.update(feedback_value = feedback)
        feedback += pid.output  # 更新反馈值
        time.sleep(0.01)
        feedback_list.append(feedback)
        setpoint_list.append(pid.setpoint)
    # 画图
    pid.visual(time_list, feedback_list, setpoint_list, END)    




# 测试代码 main 函数
def main():
    # test_pid(P = 1.2, I = 1, D = 0.001, END = 20)
    print(np.floor(2.5))
    
if __name__ == "__main__":
    main()
