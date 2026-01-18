n = int(input())
p = float(input())
b = list(map(float, input().split()))
total = 0
for num in b:
    if num > p:
        total += num
print(total)