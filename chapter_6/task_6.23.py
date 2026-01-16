n = int(input())
m = int(input())
sum_last = 0
count = 0
while n > 0 and count < m:
    sum_last += n % 10
    n //= 10
    count += 1
print(sum_last)