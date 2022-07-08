#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#===========================================================
#                        codeing
#=========================================================== 
# 创建组件
# from tkinter import Label
# widget = Label(None, text = "Hello GUI world!")
# widget.pack()
# widget.mainloop()


#=========================================================== 
# 组件尺寸调整
# from tkinter import *
# Label(text = "Hello GUI world!").pack(expand = YES, fill = X)
# Label(text = "Hello GUI world!").pack(expand = YES, fill = Y)
# Label(text = "Hello GUI world!").pack(expand = YES, fill = BOTH)
# mainloop()

#===========================================================
# 设置组件选项和窗口标题
# from tkinter import *
# widget = Label()
# widget['text'] = "Hello GUI world!"
# widget.pack(side = TOP)
# mainloop()

# from tkinter import *
# root = Tk()
# widget = Label(root)
# widget.config(text = "Hello GUI world!")
# widget.pack(side = TOP, expand = YES, fill = BOTH)
# root.title("gui1g.py")
# root.mainloop()

#===========================================================
# 添加按钮和回调函数
# import sys
# from tkinter import *
# widget = Button(None, text = "Hello widget world", command = sys.exit)
# widget.pack()
# widget.mainloop()

from tkinter import *
root = Tk()
Button(root, text = "press", command = root.quit).pack(side = LEFT)
root.mainloop()
