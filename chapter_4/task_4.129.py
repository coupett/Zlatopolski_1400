a = float(input())
b = float(input())
c = float(input())
minimal = a
if b < minimal:
    minimal = b
if c < minimal:
    minimal = c
summa = a + b + c - minimal
print(summa)