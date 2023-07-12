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
from scipy.interpolate import spline

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]


class PID:
    
    def __init__(self, P, I, D) -> None:
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.sample_time = 0.0  # TODO
        self.current_time = time.time()
        self.last_time = self.current_time
        self.clear()
    
    def clear(self):
        self.set_point = 0.0  # 设定目标值
        self.P_term = 0.0
        self.I_term = 0.0
        self.D_term = 0.0
        self.last_error = 0.0  # 上一时刻的误差
        self.int_error = 0.0  # TODO
        self.output = 0.0  # 输出
    
    def update(self, feedback_value):
        # 时间差
        self.current_time = time.time()  # 当前时间
        delta_time = self.current_time - self.last_time
        
        # 误差差分
        error = self.set_point - feedback_value  # 当前时刻误差
        delta_error = error - self.last_error
        
        if delta_time >= self.sample_time:
            self.P_term = self.Kp * error  # 比例项
            self.I_term += error * delta_time  # 积分项
            self.D_term = delta_error / delta_time if delta_time > 0.0 else 0.0  # 微分项

            self.last_time = self.current_time
            self.last_error = error
            self.output = self.P_term + (self.Ki * self.I_term) + (self.Kd * self.D_term)
        
    def set_sample_time(self, sample_time):
        self.sample_time = sample_time
 
    
    
def test_pid(P, I , D, L):
    pid = PID.PID(P, I, D)

    pid.SetPoint=1.1
    pid.setSampleTime(0.01)

    END = L
    feedback = 0
    feedback_list = []
    time_list = []
    setpoint_list = []

    for i in range(1, END):
        pid.update(feedback)
        output = pid.output
        feedback +=output #PID控制系统的函数
        time.sleep(0.01)
        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        time_list.append(i)

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    feedback_smooth = spline(time_list, feedback_list, time_smooth)
    plt.figure(0)
    plt.grid(True)
    plt.plot(time_smooth, feedback_smooth,'b-')
    plt.plot(time_list, setpoint_list,'r')
    plt.xlim((0, L))
    plt.ylim((min(feedback_list)-0.5, max(feedback_list)+0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('PythonTEST PID--xiaomokuaipao',fontsize=15)

    plt.ylim((1-0.5, 1+0.5))

    plt.grid(True)
    plt.show()




# 测试代码 main 函数
def main():
    test_pid(P = 1.2, I = 1, D = 0.001, L = 100)

if __name__ == "__main__":
    main()
