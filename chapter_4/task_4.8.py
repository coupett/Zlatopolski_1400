import math
x = float(input())
if math.sin(x) >= 0:
    k = x ** 2
else:
    k = abs(x)
if x < k:
    f = abs(x)
else:
    f = k * x
print(f)