import math
R = 6350
h = float(input())
l = math.sqrt(2 * R * h + h**2)
print(round(l, 2))