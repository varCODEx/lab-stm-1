import matplotlib.pyplot as plt
import numpy as np
from math import pow
from bisection_method import *


# x = np.arange(-5, 5, 0.1)
# y = np.float_power(3,x)-5*x**2+1
# fig, ax = plt.subplots()
# ax.plot(x,y)
# ax.grid()
# plt.show()

def f(x):
    return pow(3, x) - 5 * x ** 2 + 1


eps = 0.0001
a = -5
b = 5
print(bisection_method(f, a, b, eps))
