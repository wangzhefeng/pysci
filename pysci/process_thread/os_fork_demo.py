import os

"""
Python 程序中创建子进程
"""


print("Process (%s) start..." % os.getpid())
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print(f"I am child process ({os.getpid()}) and my parent is {os.getppid()}.")
else:
    print(f"I ({os.getpid()}) just created a child process ({pid}).")
