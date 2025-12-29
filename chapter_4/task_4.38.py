a = int(input())
b = int(input())
c = int(input())
d = int(input())
v1 = (a // c) * (b // d)
v2 = (a // d) * (b // c)
if v1 > v2:
    print("вдоль длинной")
elif v1 < v2:
    print("вдоль короткой")
else:
    print("одинаково")