n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if n ** 2 == a ** 3 + b ** 3 + c ** 3:
    print("да")
else:
    print("нет")