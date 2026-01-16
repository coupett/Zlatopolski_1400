n = int(input())
temp = n
max_digit = 0
min_digit = 9
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    temp //= 10
print("Максимальная:", max_digit)
print("Минимальная:", min_digit)