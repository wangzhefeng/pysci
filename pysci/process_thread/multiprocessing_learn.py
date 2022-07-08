import multiprocessing
import os
from multiprocessing import Pool
from multiprocessing import Process

print("当前进程ID:", os.getpid())


def action(name, *add):
    """
    定义一个函数，准备作为新进程的 target 参数

    Args:
        name ([type]): [description]
    """
    print(name)
    for arc in add:
        print(f"{arc} -- 当前进程 {os.getpid()}")




if __name__ == "__main__":
    #定义为进程方法传入的参数
    my_tuple = (
        "http://c.biancheng.net/python/",
        "http://c.biancheng.net/shell/",
        "http://c.biancheng.net/java/"
    )
    # 创建子进程，执行 action 函数
    my_process = Process(target = action, args = ("my_process 进程", *my_tuple))
    # 启动子进程
    my_process.start()
    # 主进程执行该函数
    action("主进程", *my_tuple)
    print("CPU 核心数量: ", str(multiprocessing.cpu_count()))
