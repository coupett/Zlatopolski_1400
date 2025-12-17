n = int(input())
a = n // 10
b = n % 10
if a > b:
    print("первая")
elif a < b:
    print("вторая")
else:
    print("равны")
if a == b:
    print("да")
else:
    print("нет")