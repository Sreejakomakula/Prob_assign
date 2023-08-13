import numpy as np
import math

# Coordinates of points A, B, C, and O
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])
O = np.array([-53/12, 5/12])

# Calculate the direction vectors of OA, OB, and OC
OA = A - O
OB = B - O
OC = C - O

# Calculate the lengths of OA, OB, and OC
length_OA = math.sqrt(np.dot(OA, OA))
length_OB = math.sqrt(np.dot(OB, OB))
length_OC = math.sqrt(np.dot(OC, OC))

# Print the lengths of OA, OB, and OC
print("Length of OA:", length_OA)
print("Length of OB:", length_OB)
print("Length of OC:", length_OC)

# Check if the lengths are approximately equal
if math.isclose(length_OA, length_OB) and math.isclose(length_OB, length_OC):
    print("OA = OB = OC")
else:
    print("OA, OB, and OC are not equal")

