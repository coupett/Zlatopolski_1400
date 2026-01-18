a = list(map(float, input().split()))
total = 0
for num in a:
    if num > 10.75:
        total += num
print(total)