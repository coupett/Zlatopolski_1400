a3 = int(input())
a2 = int(input())
a1 = int(input())
b2 = int(input())
b1 = int(input())
if a1 >= b1:
    e1 = a1 - b1
    z1 = 0
else:
    e1 = a1 + 10 - b1
    z1 = 1
temp = a2 - b2 - z1
if temp < 0:
    e2 = temp + 10
    z2 = 1
else:
    e2 = temp
    z2 = 0
e3 = a3 - z2
print(e3)
print(e2)
print(e1)