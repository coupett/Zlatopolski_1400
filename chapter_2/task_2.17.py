import math
a = int(input())
b = int(input())
h = int(input())
c = math.sqrt(h**2 + ((b - a)/2)**2)
p = a + b + 2*c
print(p)