n = int(input())
a = int(input())
x1 = n // 1000
x2 = n // 100 % 10
x3 = n // 10 % 10
x4 = n % 10
if (x1 + x2) == (x3 + x4):
    print("да")
else:
    print("нет")
s = x1 + x2 + x3 + x4
if s % 3 == 0:
    print("да")
else:
    print("нет")
p = x1 * x2 * x3 * x4
if p % 4 == 0:
    print("да")
else:
    print("нет")
if p % a == 0:
    print("да")
else:
    print("нет")