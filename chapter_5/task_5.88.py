s = int(input())
count = 0
for num in range(100, 1000):
    sum_digits = num//100 + (num//10)%10 + num%10
    if sum_digits == s:
        count += 1
print(count)