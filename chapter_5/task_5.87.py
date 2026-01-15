count = 0
for num in range(100, 501):
    sum_digits = num//100 + (num//10)%10 + num%10
    if sum_digits == 15:
        count += 1
print(count)