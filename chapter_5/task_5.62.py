a = float(input())
n = int(input())
result = 1
for _ in range(abs(n)):
    result *= a
if n < 0:
    result = 1 / result
print(result)