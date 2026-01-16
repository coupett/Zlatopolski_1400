n = int(input())
temp = n
first_digit = 0
count = 0
while temp > 0:
    digit = temp % 10
    if temp == n:
        first_digit = digit
    if digit == first_digit:
        count += 1
    temp //= 10
print(count)