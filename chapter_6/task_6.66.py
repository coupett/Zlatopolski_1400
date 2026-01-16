def nod(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a = int(input())
b = int(input())
c = int(input())

result = nod(nod(a, b), c)
print("НОД трех чисел:", result)