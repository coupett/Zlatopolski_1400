n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if a == b == c:
    print("да")
else:
    print("нет")
if a == b or a == c or b == c:
    print("да")
else:
    print("нет")