# Solving Ax = b using steepest descent method
# Equation: Equation 1: x - y = -10
#           Equation 2: 2x + 3y = 15
# A = [1,-1; 2,3] and b = [-10; 15]

import numpy as np

A = np.zeros((2,2))         # Define A matrix
A[0,0] = 1.0
A[0,1] = -1.0
A[1,0] = 2.0
A[1,1] = 3.0

b = np.zeros((2,1))         # Define b vector
b[0] = -10.0
b[1] = 15.0

res = np.ones((2,1))        # Define the residue res = b - Ax
res[0] = 10
res[1] = 10

x = np.ones((2,1))          # Initial guess solution
x[0] = 0
x[1] = 0

count = 0
while res[0] > 0.001 or res[1] > 0.001:
    res = b - np.dot(A, x)
    p = np.dot(np.transpose(res),A)
    q = np.dot(p,res)
    alp = (np.dot((np.transpose(res)), res)) / float(q)
    x = x + alp*res
    count = count+1

print ("Actual solution is: ")
print (np.dot(np.linalg.inv(A),b))

print ("Iterative Solution x is:  ")
print (x)

print ("The final residue is:   ")
print (res)

print ("Number of iterations are:   ")
print (count)
