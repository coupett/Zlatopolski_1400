import math
r = float(input())
a = float(input())
s_krug = math.pi * r ** 2
s_kvadrat = a ** 2
if s_krug > s_kvadrat:
    print("круг")
elif s_krug < s_kvadrat:
    print("квадрат")
else:
    print("равны")