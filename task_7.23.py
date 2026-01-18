a = list(map(float, input().split()))
product = 1
for num in a:
    product *= num
print(product < 10000)