a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("угрожает")
else:
    print("не угрожает")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d):
    print("угрожает")
else:
    print("не угрожает")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) <= 1 and abs(b - d) <= 1 and not (a == c and b == d):
    print("может")
else:
    print("не может")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d or abs(a - c) == abs(b - d):
    print("угрожает")
else:
    print("не угрожает")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b == 2:
    if c == a and d == b + 2:
        print("может")
    elif c == a and d == b + 1:
        print("может")
    else:
        print("не может")
else:
    if c == a and d == b + 1:
        print("может")
    else:
        print("не может")
if abs(a - c) == 1 and d == b + 1:
    print("может")
else:
    print("не может")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b == 7:
    if c == a and d == b - 2:
        print("может")
    elif c == a and d == b - 1:
        print("может")
    else:
        print("не может")
else:
    if c == a and d == b - 1:
        print("может")
    else:
        print("не может")
if abs(a - c) == 1 and d == b - 1:
    print("может")
else:
    print("не может")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
dx = abs(a - c)
dy = abs(b - d)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("угрожает")
else:
    print("не угрожает")