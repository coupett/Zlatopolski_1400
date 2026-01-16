a = int(input())
b = int(input())

x, y = a, b
while y != 0:
    x, y = y, x % y
nod = x

nok = a * b // nod
print("НОК:", nok)