import math
s_krug = float(input())
s_treug = float(input())
r = math.sqrt(s_krug / math.pi)
a = math.sqrt(4 * s_treug / math.sqrt(3))
h_treug = a * math.sqrt(3) / 2
r_vpis = a * math.sqrt(3) / 6
r_opis = a * math.sqrt(3) / 3
if 2 * r <= h_treug:
    print("да")
else:
    print("нет")
if r_opis <= r:
    print("да")
else:
    print("нет")