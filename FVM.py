import numpy as np
import matplotlib
from matplotlib import pyplot as plt

k = 5000   # J/m sec

x_max = 8   # Domain length
x_points = 101   # Number of nodes
n_ele = x_points - 1    # Number of elements or control volumes
n_grid_points = x_points + 1    # Number of centroid points to consider
len_ele = x_max/float(n_ele)    # Length of an element

x = np.zeros(n_grid_points)
x[0] = 0
x[1] = x[0] + len_ele/float(2)
x[-1] = x_max
x[-2] = x[-1] - len_ele/float(2)
for i in range(2, n_grid_points-2):
    x[i] = x[i-1] + len_ele

T = np.zeros(n_grid_points)
T[0] = 0
T[1] = T[0]

a1 = k/float(len_ele/2)
a3 = k/float(len_ele/2)
a2 = a1 + a3
for i in range(2, n_grid_points):
    T[i] = (a2*T[i-1] - a1*T[i-2] - (3+4*T[i-1]))/float(a3)

plt.plot(x,T)
plt.show()

