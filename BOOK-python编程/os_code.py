#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


#===========================================================
#                        codeing
#===========================================================
# os
print(dir(os))
print("-" * 100)
print(dir(os.path))
print("-" * 100)
print(os.getpid())
print("-" * 100)
print(os.getcwd())
print("-" * 100)
os.chdir(r"E:\project\projects\python")
print(os.getcwd())
os.chdir(r"E:\project\projects")
print("-" * 100)
print(os.pathsep) # ';'
print(os.sep)	  # '\'
print(os.pardir)  # '..'
print(os.curdir)  # '.'
print(os.linesep) # '\r\n'
print("-" * 100)
#===========================================================
# os.path
print(os.path.isdir(r'E:\project'))
print(os.path.isfile(r'E:\project'))
print(os.path.exists(r'E:\project\projects'))
print(os.path.getsize(r'E:\project\projects\test.py'))
print(os.path.split(r'E:\project\projects\test.py'))
print(os.path.join(r'E:\project', 'test.py'))
name = r'E:\project\test.py'
print(os.path.dirname(name), os.path.basename(name))
print(os.path.splitext(r'E:\project\projects\test.py'))
print(os.sep)
pathname = r'E:\project\projects\test.py'
print(os.path.split(pathname))
print(pathname.split(os.sep))
print(os.sep.join(pathname.split(os.sep)))
print(os.path.join(*pathname.split(os.sep)))
mixed = r'C:\temp\public/files/index.html'
print(mixed)
print(os.path.normpath(mixed))
print(os.path.normpath(r'C:\temp\\sub\.\file.ext'))
os.chdir(r'E:\project')

print(os.getcwd())
print(os.path.abspath(""))
print(os.path.abspath("projects"))
print(os.path.abspath(r"projects\python"))
print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.abspath(r"..\documents"))
print(os.path.abspath(r"E:\project\projects\test.py"))
print(os.path.abspath(r"E:\project\projects"))
print("*" * 100)

#===========================================================
# shell命令
os.chdir(r"E:\project\projects")
os.getcwd()
os.system("dir")
os.system("type sys_code.py")


open("test.py").read()
text = os.popen("type test.py").read()
print(text)
listing = os.popen("dir").readlines()
print(listing)

#===========================================================
# subprocess
import subprocess
subprocess.call("python test.py")
# subprocess.call("cmd /E 'type test.py'")
subprocess.call("type test.py", shell = True)
print('\n' + '-' * 100)

pipe = subprocess.Popen("python test.py", stdout = subprocess.PIPE)
print(pipe.communicate())
print(pipe.returncode)