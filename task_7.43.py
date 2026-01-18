numbers = list(map(int, input().split()))
total = 0
for num in numbers:
    if num % 10 == 0:
        total += num
print(total)