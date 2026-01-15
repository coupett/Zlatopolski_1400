a = float(input())
n = int(input())
result = 0
for _ in range(abs(n)):
    result += a
if n < 0:
    result = -result
print(result)