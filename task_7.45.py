c = list(map(float, input().split()))
total = 0
for i in range(0, 15, 2):
    total -= c[i]
print(total)