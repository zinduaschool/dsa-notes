import random as rn
import math

p = 1000000
n = 0 #points in the circle

for i in range(p):
    x = rn.random()
    y = rn.random()
    z = math.sqrt(x**2 + y**2)

    if z <= 1:
        n += 1

print((4*n)/p)