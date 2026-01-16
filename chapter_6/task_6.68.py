a = int(input())
b = int(input())

x, y = a, b
while y != 0:
    x, y = y, x % y
nod = x

p = a // nod
q = b // nod
print(f"{p}/{q}")