n = int(input())
x = n % 10 * 100 + n // 10 % 10 * 10 + n // 100
print(x)