n = int(input())
s = n // 1000 + n // 100 % 10 + n // 10 % 10 + n % 10
print(s)

n = int(input())
s = n // 10000 + n // 1000 % 10 + n // 100 % 10 + n // 10 % 10 + n % 10
print(s)