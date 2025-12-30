a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0
if a % 3 == 0:
    s += a
if b % 3 == 0:
    s += b
if c % 3 == 0:
    s += c
if d % 3 == 0:
    s += d
print(s)