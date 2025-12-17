import math
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
else:
    print("корней нет")