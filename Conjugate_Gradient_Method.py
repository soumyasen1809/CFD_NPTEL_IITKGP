# Solving Ax = b using conjugate gradient method
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

res = b - np.dot(A, x)
temp = np.dot(np.transpose(res),A)
temp0 = np.dot(temp,res)
alp = (np.dot((np.transpose(res)), res)) / float(temp0)     # Magnitude of search direction
x = x + alp*res
p = res                     # Initial search direction is same as residue
count = 0
while res[0] > 0.001 or res[1] > 0.001:
    res = b - np.dot(A, x)
    temp1 = np.dot(np.transpose(p),A)
    temp2 = np.dot(temp1,res)
    temp3 = np.dot(np.transpose(p),A)
    temp4 = np.dot(temp3,p)
    beta = temp2/float(temp4)

    p = res - beta*p        # Subsequent search directions
    temp5 = np.dot(np.transpose(p),res)
    temp6 = np.dot(np.transpose(p),A)
    temp7 = np.dot(temp6, p)
    alp = temp5/float(temp7)

    x = x + alp*p
    count = count+1         # Counts number of iterations

print ("Actual solution is: ")
print (np.dot(np.linalg.inv(A),b))

print ("Iterative Solution x is:  ")
print (x)

print ("The final residue is:   ")
print (res)

print ("Number of iterations are:   ")
print (count)
