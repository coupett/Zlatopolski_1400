n = int(input())
a = int(input())
d1 = n // 10
d2 = n % 10
if d1 == 3 or d2 == 3:
    print("да")
else:
    print("нет")
if d1 == a or d2 == a:
    print("да")
else:
    print("нет")