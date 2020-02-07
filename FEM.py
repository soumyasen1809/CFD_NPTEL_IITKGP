import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# Define parameters
Q = 100 # J/m2 sec
A = 10  #m2
k = 0.005   # J/m sec

# Discretization
x_max = 0.08    # Domain length is 8 cm
x_points = 101    # Number of nodes
n_ele = x_points - 1    # Number of elements
len_ele = x_max/float(n_ele)    # Length of an element

x = np.linspace(0,x_max, x_points)
K_gl = np.zeros((x_points, x_points))  # Global Stiffness
T_gl = np.zeros(x_points)              # Find temperature distribution
f_gl = np.zeros(x_points)              # Global Force

K_ele = np.zeros((2,2))                # Elemental stiffness
f_ele = np.zeros(2)                    # Elemental force

# Solving for element
for i in range(0, 2):
    for j in range(0,2):
        K_ele[i,j] = np.power(-1, (i+j))*(k/float(len_ele))
    f_ele[i] = (Q/(k*float(A)))*len_ele/float(2)

# Assembly
for i in range(0, x_points-1):
    for j in range(0, x_points-1):
        if i == j:
            K_gl[i, j] = K_gl[i, j] + K_ele[0, 0]
            K_gl[i, j + 1] = K_gl[i, j + 1] + K_ele[0, 1]
            K_gl[i + 1, j] = K_gl[i + 1, j] + K_ele[1, 0]
            K_gl[i + 1, j + 1] = K_gl[i + 1, j + 1] + K_ele[1, 1]
    f_gl[i] = f_gl[i] + f_ele[0]
    f_gl[i+1] = f_gl[i+1] + f_ele[1]

f_gl[0] = 0
f_gl[-1] = 15+(Q/(k*float(A)))*len_ele/float(2)     # Imposing natural boundary condition, heat flux at x = 8 cm

K_gl_2 = np.zeros((x_points-2, x_points-2))     # Global Stiffness after addition of BCs
T_gl_2 = np.zeros(x_points-2)                   # Find temperature distribution
f_gl_2 = np.zeros(x_points-2)                   # Global Force considering BCs

for i in range(0, x_points - 2):
    for j in range(0, x_points - 2):
        K_gl_2[i,j] = K_gl[i+1,j+1]
    f_gl_2[i] = f_gl[i+1]

K_gl_2_inv = np.linalg.inv(K_gl_2)
T_gl_2 = np.dot(K_gl_2_inv, f_gl_2)

for i in range(0, x_points-2):
    T_gl[i+1] = T_gl_2[i]

print (T_gl)
plt.plot(x, T_gl)
plt.show()
