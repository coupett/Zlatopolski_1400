import math

a = int(input())
b = int(input())
u = int(input())

u_r = math.radians(u)
h = (a - b) / 2 * math.tan(u_r)
area = (a + b) * h /2
print(area)