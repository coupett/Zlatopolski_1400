n = int(input())
a = int(input())
b = int(input())

temp = n
count_a = 0
count_b = 0

while temp > 0:
    digit = temp % 10
    if digit == a:
        count_a += 1
    if digit == b:
        count_b += 1
    temp //= 10

print(count_a < count_b)