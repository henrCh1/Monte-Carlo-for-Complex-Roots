# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:46:16 2023

@author: 86319
"""

import random as ra

# 数值定义区
# 初值x0的实部
x0_real = 1
# 初值x0的虚部
x0_imag = 1
# 初始半径
radius = 300
# 误差限度
eps = 1e-4
# 随机次数上限
max_iterations = 1e+3

# 定义需要运算的函数
def f(x):
    return x**2 - 6*x + 13

# 蒙特卡罗求解一元方程
def monte_carlo_equation_solver(x0_real, x0_imag, radius, eps, max_iterations):
    # 计算游动次数
    iterations = 0
    # complex(a,b)表示复数a+bi
    while abs(f(complex(x0_real, x0_imag)).real) + abs(f(complex(x0_real, x0_imag)).imag) > eps:
        x1_real = x0_real + radius * (2 * ra.random() - 1)
        x1_imag = x0_imag + radius * (2 * ra.random() - 1)
        iterations += 1
        if abs(f(complex(x1_real, x1_imag)).real) + abs(f(complex(x1_real, x1_imag)).imag) < abs(f(complex(x0_real, x0_imag)).real) + abs(f(complex(x0_real, x0_imag)).imag):
            # 如果每个方程的总值比随机前小时，就选取这个点为新的起点
            x0_real = x1_real
            x0_imag = x1_imag
        # 重置半径的值，压缩x0的游动范围
        elif iterations == max_iterations:
            radius = radius / 2
            iterations = 0
            x0_real, x0_imag = 1, 1
    return x0_real, x0_imag

# 调用函数并输出结果
s, i = monte_carlo_equation_solver(x0_real, x0_imag, radius, eps, max_iterations)
print("方程实部：{}".format(s), "方程虚部：{}".format(i))
