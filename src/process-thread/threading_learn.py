import time
import threading

"""
Python 多线程编程
"""

def action_1(add):
    """
    定义线程要调用的方法
    """
    for arc in add:
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)

def action_2(*add):
    """
    定义线程要调用的方法
    """
    for arc in add:
        # 暂停 0.1 秒后再执行
        time.sleep(0.1)
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)


class my_Thread(threading.Thread):
    """
    创建子线程类

    Args:
        threading ([type]): 继承自 Thread 类
    """
    def __init__(self, add):
        threading.Thread.__init__(self)
        self.add = add
    
    def run(self):
        """
        重写 run 方法
        """
        for arc in self.add:
            # 调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() + " " + arc)








# 定义线程方法传入的参数
my_tuple = [
    "http://c.biancheng.net/python/",
    "http://c.biancheng.net/shell/",
    "http://c.biancheng.net/java/"
]
# ---------------
# 
# ---------------
# action_1(my_tuple)
# for i in range(5):
#     print(threading.current_thread().getName())
# ---------------
# 
# ---------------
# 创建线程
thread = threading.Thread(target = action_2, args = my_tuple)

# 将 thread 设置为守护线程
# thread.daemon = True

# 启动线程
thread.start()

# 指定 thread 线程优先执行完毕
# thread.join()

# 主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())
# ---------------
# 
# ---------------
# 创建线程
# mythread = my_Thread(my_tuple)
# 启动线程
# mythread.start()
# for i in range(5):
#     print(threading.current_thread().getName())
    
