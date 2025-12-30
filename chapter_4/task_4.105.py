a = float(input())
b = float(input())
if a < 0:
    a = -a
if b < 0:
    b = -b
if a > b:
    a = a / 2
print(a)