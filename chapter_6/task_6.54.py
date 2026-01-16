n = int(input())
temp = n
count_0 = 0
count_9 = 0

while temp > 0:
    digit = temp % 10
    if digit == 0:
        count_0 += 1
    if digit == 9:
        count_9 += 1
    temp //= 10

if count_0 > count_9:
    print("0")
elif count_9 > count_0:
    print("9")
else:
    print("одинаково")