m = int(input())
n = int(input())
for i in range(1, m*n + 1):
    print(i * m * n // (m * n))