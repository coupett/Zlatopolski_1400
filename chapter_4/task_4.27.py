n = int(input())
a = n // 10
b = n % 10
if n ** 2 == 4 * (a ** 3 + b ** 3):
    print("да")
else:
    print("нет")