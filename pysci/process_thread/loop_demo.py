# -*- coding: utf-8 -*-


# *********************************************
# * Author      : zhefeng wang
# * Email       : wangzhefengr@163.com
# * Date        : 2021.01.01
# * Version     : 1.0.0
# * Description : description
# * Link        : link
# **********************************************


# python libraries
import os
import sys
import functools
import time
import timeit
import threading
import multiprocessing


# global variable
GLOBAL_VARIABLE = None


# **********************************************
# * 1.分析代码运行时间
# **********************************************
def timeit_func(func):
    """
    functools 模块提供了两个装饰    
    wraps 装饰器：
        1.函数有几个特殊属性比如函数名，在被装饰后，函数名会变成包装函数的名字 wrapper
        2.如果希望使用反射，可能会导致意外的结果，这个装饰器可以解决这个问题，它能将装饰过的函数的特殊属性保留

    Args:
        func ([type]): [description]
    """
    @functools.wraps(func)
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"used: {end - start}")
    
    return wrapper

def test_1():
    # method 1
    @timeit_func
    def g():
        return 1 ** 2 + 1
    
    g()

    # method 2
    timeit.timeit("g()", globals = { "main": main }, number = 10)

# **********************************************
# 应用多线程加速IO密集型任务
# **********************************************
def writefile(i):
    with open(str(i) + ".txt", "w") as f:
        s = (f"hello {i}") * 10000000
        f.write(s)

# 串行
for i in range(10):
    writefile(i)

# 多线程
thread_list = []
for i in range(10):
    t = threading.Thread(target = writefile, args = (i,))
    # 设置为守护进程
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    # 启动线程
    t.start()

for t in thread_list:
    # 等待子线程结束
    t.join()

# **********************************************
# * 应用多进程加速 CPU 密集型任务
# **********************************************
def much_job(x):
    time.sleep(5)
    return (x ** 2)

# 串行
ans = [much_job(i) for i in range(8)]
print(ans)

# 多进程
pool = multiprocessing.Pool(processes = 4)
result = []
for i in range(8):
    result.append(pool.apply_async(much_job, (i,)))
pool.close()
pool.join()

ans = [res.get() for res in result]
print(ans)





# 测试代码 main 函数
def main():
    test_1()


if __name__ == "__main__":
    main()

