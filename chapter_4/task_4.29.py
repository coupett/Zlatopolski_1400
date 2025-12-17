n = int(input())
a = int(input())
s = n // 10 + n % 10
if s % 3 == 0:
    print("да")
else:
    print("нет")
if s % a == 0:
    print("да")
else:
    print("нет")