n = int(input())
d1 = n // 1000
d2 = n // 100 % 10
d3 = n // 10 % 10
d4 = n % 10
if d1 == 2 or d1 == 7 or d2 == 2 or d2 == 7 or d3 == 2 or d3 == 7 or d4 == 2 or d4 == 7:
    print("да")
else:
    print("нет")
if d1 == 3 or d1 == 6 or d1 == 9 or d2 == 3 or d2 == 6 or d2 == 9 or d3 == 3 or d3 == 6 or d3 == 9 or d4 == 3 or d4 == 6 or d4 == 9:
    print("да")
else:
    print("нет")