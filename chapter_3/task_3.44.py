a3 = int(input())
a2 = int(input())
a1 = int(input())
b2 = int(input())
b1 = int(input())
e1 = (a1 + b1) % 10
p1 = (a1 + b1) // 10
s2 = a2 + b2 + p1
e2 = s2 % 10
p2 = s2 // 10
e3 = a3 + p2
print(e3)
print(e2)
print(e1)