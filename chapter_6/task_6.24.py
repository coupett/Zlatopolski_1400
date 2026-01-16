n = int(input())
sign = 1
sum_a = 0
while n > 0:
    digit = n % 10
    sum_a += sign * digit
    sign = -sign
    n //= 10
print(sum_a)