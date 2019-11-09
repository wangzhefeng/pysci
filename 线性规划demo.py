'''
线性规划demo

求解 max z = 2x1 + 3x2 - 5x3
s.t. x1 + x2 + x3 = 7
	2x1 - 5x2 + x3 >= 10
	x1 + 3x2 + x3 <= 12
	x1, x2, x3 >= 0

scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None, options=None)
    - c 函数系数数组，最大化参数为c，最小化为-c，函数默认计算最小化。
    - A_ub 不等式未知量的系数，默认转成 <= ，如果原式是 >= 系数乘负号。
    - B_ub 对应A_ub不等式的右边结果
    - A_eq 等式的未知量的系数
    - B_eq 等式的右边结果
    - bounds 每个未知量的范围
'''

from scipy import optimize as op
import numpy as np

c = np.array([2,3,-5])
A_ub = np.array([[-2,5,-1],[1,3,1]])
B_ub = np.array([-10,12])
A_eq = np.array([[1,1,1]])
B_eq = np.array([7])
x1 = (0,7)
x2 = (0,7)
x3 = (0,7)
res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3))

print(res)

'''
     con: array([0.])
     fun: -14.571428571428571
 message: 'Optimization terminated successfully.'
     nit: 8
   slack: array([0.        , 3.85714286])
  status: 0
 success: True
       x: array([6.42857143, 0.57142857, 0.        ])

fun: -14.571428571428571 是最小化的结果，我们取的-c所以最大化结果是14.57...
x: array([6.42857143, 0.57142857, 0.        ]) 是线性规划问题中的x1, x2, x3结果。
'''