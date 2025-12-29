a1 = float(input())
a2 = float(input())
a3 = float(input())
b1 = float(input())
b2 = float(input())
b3 = float(input())
al = sorted([a1, a2, a3])
bl = sorted([b1, b2, b3])
if bl[0] <= al[0] and bl[1] <= al[1] and bl[2] <= al[2]:
    print("сможет")
else:
    print("не сможет")