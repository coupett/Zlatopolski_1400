n = int(input())
d1 = n // 10
d2 = n % 10
if d1 == 4 or d1 == 7 or d2 == 4 or d2 == 7:
    print("да")
else:
    print("нет")
if d1 == 3 or d1 == 6 or d1 == 9 or d2 == 3 or d2 == 6 or d2 == 9:
    print("да")
else:
    print("нет")