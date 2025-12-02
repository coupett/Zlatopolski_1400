n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(d * 1000 + c * 100 + b * 10 + a)

n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(b * 1000 + a * 100 + d * 10 + c)

n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
print(a * 1000 + c * 100 + b * 10 + d)

n = int(input())
print((n % 100) * 100 + n // 100)