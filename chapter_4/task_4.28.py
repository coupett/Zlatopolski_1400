n = int(input())
a = int(input())
s = n // 10 + n % 10
if s >= 10:
    print("да")
else:
    print("нет")
if s > a:
    print("да")
else:
    print("нет")