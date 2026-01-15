x = float(input())
n = int(input())
total = 1
fact = 1
power = 1
for i in range(1, n + 1):
    fact *= i
    power *= x
    total += power / fact
print(total)