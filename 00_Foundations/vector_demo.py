import math

print("Vector Calculator")

# get vector A
Ax = float(input("Enter Ax: "))
Ay = float(input("Enter Ay: "))

# get vector B
Bx = float(input("Enter Bx: "))
By = float(input("Enter By: "))

# vector addition
C = (Ax + Bx, Ay + By)

# magnitude of A
magA = math.sqrt(Ax*Ax + Ay*Ay)

print("A + B =", C)
print("Magnitude of A =", magA)
