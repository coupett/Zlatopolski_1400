import math
x = float(input())
if x > 0:
    y = math.sin(x) ** 2
else:
    y = 1 - 2 * math.sin(x ** 2)
print(y)