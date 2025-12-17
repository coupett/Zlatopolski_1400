n = int(input())
a = int(input())
x = n // 100
y = n // 10 % 10
z = n % 10
s = x + y + z
p = x * y * z
if s >= 10:
    print("да")
else:
    print("нет")
if p >= 100:
    print("да")
else:
    print("нет")
if p > a:
    print("да")
else:
    print("нет")
if s % 5 == 0:
    print("да")
else:
    print("нет")
if s % a == 0:
    print("да")
else:
    print("нет")