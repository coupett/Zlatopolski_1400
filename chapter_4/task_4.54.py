n = int(input())
b = int(input())
d1 = n // 1000
d2 = n // 100 % 10
d3 = n // 10 % 10
d4 = n % 10
if d1 == 4 or d2 == 4 or d3 == 4 or d4 == 4:
    print("да")
else:
    print("нет")
if d1 == b or d2 == b or d3 == b or d4 == b:
    print("да")
else:
    print("нет")