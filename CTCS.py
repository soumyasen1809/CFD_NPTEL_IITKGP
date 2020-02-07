import numpy as np
import matplotlib
from matplotlib import pyplot as plt

x_max = 1       # Domain in X
x_points = 11   # Number of grid points
t_points = 51   # Number of time steps

alp = 1.0
del_x = 0.5
del_t = 0.1
r = alp*(del_t/float(del_x**2))       # CFL stability criteria; always unconditionally unstable; r = alp*(del_t/del_x^2)

x = np.linspace(0, x_max, x_points)
T = np.zeros(x_points)
T_new = np.zeros(x_points)
T_old = np.zeros(x_points)

for ix in range(0, x_points):
    if x[ix] > 0.2 and x[ix] < 0.5:
        T[ix] = 2

for it in range(0, t_points):
    for ix in range(1, x_points-1):
        T_new[ix] = T_old[ix] + 2*r*(T[ix+1] - 2*T[ix] + T[ix-1])

    T_new[0] = 0
    T_new[-1,] = T_new[-2,]

    T_old = T.copy()
    T = T_new.copy()

plt.plot(x, T)
plt.show()
