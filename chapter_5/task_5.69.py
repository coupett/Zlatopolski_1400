n = int(input())
total = 1
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += 1 / fact
print(total)