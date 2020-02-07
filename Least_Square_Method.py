import numpy as np
import matplotlib
from matplotlib import pyplot as plt

x_max = 1   # Length of the domain
x_points = 100  # Number of points

x = np.linspace(0, x_max, x_points)
u = np.zeros(x_points)      # Solution vector u
d2u = np.zeros(x_points)    # 2nd derivative of u
R = np.zeros(x_points)      # Residue
a = 1.0/float(2*np.pi)      # Calculated based on least square method
for i in range(0, x_points - 1):
    u[i] = a*np.sin(x[i] * np.pi)
    d2u[i] = -1*np.pi*(a**2)*np.sin(x[i] * np.pi)
    R[i] = d2u[i] + u[i] + x[i]

plt.plot(x,u)
plt.plot(x,R)
plt.show()
