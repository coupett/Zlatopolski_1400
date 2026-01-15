import math
p0 = 1.29
z = 1.25e-4
for h in range(0, 1100, 100):
    p = p0 * math.exp(-h * z)
    print(h, p)