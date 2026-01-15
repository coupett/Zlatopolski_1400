import math
area = 0
step = 0.001
x = 0
while x <= math.pi:
    area += math.sin(x) * step
    x += step
print(area)