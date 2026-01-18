d = list(map(int, input().split()))
total = 0
for num in d:
    if num % 2 == 0:
        total += num
print(total)