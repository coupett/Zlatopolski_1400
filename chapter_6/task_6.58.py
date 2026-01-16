n = int(input())

# Способ 1 (два цикла)
temp = n
max_digit = 0
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10

temp = n
count = 0
while temp > 0:
    digit = temp % 10
    if digit == max_digit:
        count += 1
    temp //= 10

print("Способ 1:", count)

# Способ 2 (один цикл)
temp = n
max_digit = 0
count = 0
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
        count = 1
    elif digit == max_digit:
        count += 1
    temp //= 10

print("Способ 2:", count)