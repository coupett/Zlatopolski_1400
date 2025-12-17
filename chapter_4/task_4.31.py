n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if a > c:
    print("первая")
elif a < c:
    print("последняя")
else:
    print("равны")
if a > b:
    print("первая")
elif a < b:
    print("вторая")
else:
    print("равны")
if b > c:
    print("вторая")
elif b < c:
    print("последняя")
else:
    print("равны")