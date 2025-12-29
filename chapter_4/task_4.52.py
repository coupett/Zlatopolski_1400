n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if a == 6 or b == 6 or c == 6:
    print("да")
else:
    print("нет")