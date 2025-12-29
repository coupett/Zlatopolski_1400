import math
x = float(input())
if 0.2 <= x <= 0.9:
    f = math.sin(x)
else:
    f = 1
print(f)