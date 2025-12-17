v1 = float(input())
v2 = float(input())
v1_ms = v1 * 1000 / 3600
if v1_ms > v2:
    print(1)
elif v1_ms < v2:
    print(2)
else:
    print(0)