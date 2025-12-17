import math
s_krug = float(input())
s_kvadrat = float(input())
r = math.sqrt(s_krug / math.pi)
a = math.sqrt(s_kvadrat)
d_krug = 2 * r
d_kvadrat = a * math.sqrt(2)
if d_krug <= a:
    print("да")
else:
    print("нет")
if d_kvadrat <= 2 * r:
    print("да")
else:
    print("нет")