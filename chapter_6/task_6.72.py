n = int(input())
f = int(input())
s = int(input())

if s == 0:
    if n == f:
        print("является")
    else:
        print("не является")
else:
    if (n - f) % s == 0 and (n - f) // s >= 0:
        print("является")
    else:
        print("не является")