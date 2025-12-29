k = int(input())
day = (k - 1) % 7
if day >= 5:
    print("выходной")
else:
    print("рабочий")