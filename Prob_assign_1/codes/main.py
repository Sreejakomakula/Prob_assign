import numpy as np

# Given points A, B, and C
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])

# Direction vector of BC
BC = C - B

# Direction vector of AD1
AD1_direction = np.array([np.dot(0,BC[0])+np.dot(1,BC[1]),np.dot(-1,BC[0])+np.dot(0,BC[1])])

# Find the normal vector of AD1
normal_vector= np.array([np.dot(0,AD1_direction [0])+np.dot(1,AD1_direction [1]),np.dot(-1,AD1_direction [0])+np.dot(0,AD1_direction [1])])

print("Given points:")
print("A:", A)
print("B:", B)
print("C:", C)
print("Direction vector of BC:", BC)
print("Direction vector of AD1:", AD1_direction)
print("Normal vector of AD1_1:",normal_vector)

