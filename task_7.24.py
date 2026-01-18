n = int(input())
s = float(input())
d = list(map(float, input().split()))
product = 1
for num in d:
    product *= num
print(product > s)