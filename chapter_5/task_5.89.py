count = 0
for num in range(100, 1000):
    if num % 7 == 0:
        sum_digits = num//100 + (num//10)%10 + num%10
        if sum_digits % 7 == 0:
            count += 1
print(count)