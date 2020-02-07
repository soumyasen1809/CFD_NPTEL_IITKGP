# Differential equation is: dy/d(theta) = 2*(1-theta)
# Using Finite Volume Method:   theta_e - theta_w = 2*delta_y*(1-theta_p)
# Or, ap*theta_p = ae*theta_e + aw_theta_w + b, where ae = 0, aw = 1, ap = 1+2*delta_y, b = 2*delta_y

import numpy as np
from matplotlib import pyplot as plt
x_points = 5   # Number of grid points
del_x = 0.25
x = np.linspace(0, 1, x_points)
theta = np.zeros(x_points)
ae = 0
aw = 1
ap = 1+2*del_x
b = 2*del_x

# Numerical Upwind scheme solution
for i in range(1,x_points-1):
    theta[i] = (ae*theta[i+1] + aw*theta[i-1] + b)/float(ap)

theta[0] = 0.0      # Adding the boundary conditions
theta[-1] = (aw*theta[-2] + b)/float(ap)


print ("Numerical solution")
print (theta)

# Analytical Solution
theta_an = 1 - np.exp(-2*x)

print ("Analytical solution")
print (theta_an)

# Plotting the solutions
plt.plot(x,theta)
plt.plot(x, theta_an)
plt.show()
