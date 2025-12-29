n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if a == 4 or a == 7 or b == 4 or b == 7 or c == 4 or c == 7:
    print("да")
else:
    print("нет")
if a == 3 or a == 6 or a == 9 or b == 3 or b == 6 or b == 9 or c == 3 or c == 6 or c == 9:
    print("да")
else:
    print("нет")