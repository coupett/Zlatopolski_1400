k = int(input())
day = (k - 1) % 7
if day == 5:
    print("суббота")
elif day == 6:
    print("воскресенье")
else:
    print("рабочий")

k = int(input())
d = int(input())
day = (k - 1 + d - 1) % 7
if day == 5:
    print("суббота")
elif day == 6:
    print("воскресенье")
else:
    print("рабочий")