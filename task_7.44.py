a = list(map(int, input().split()))
total = 0
for i in range(1, 20, 2):
    total += a[i]
print(total)