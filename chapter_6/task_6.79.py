n = int(input())
temp = n
prev = 10
is_ordered = True

while temp > 0:
    digit = temp % 10
    if digit > prev:
        is_ordered = False
        break
    prev = digit
    temp //= 10

print(is_ordered)