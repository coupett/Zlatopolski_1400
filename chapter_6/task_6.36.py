n = int(input())
a = int(input())
x = int(input())
y = int(input())

temp = n
count_a = 0
sum_gt_a = 0
sum_even = 0
count_xy = 0

while temp > 0:
    digit = temp % 10
    if digit == a:
        count_a += 1
    if digit > a:
        sum_gt_a += digit
    if digit % 2 == 0:
        sum_even += digit
    if digit == x or digit == y:
        count_xy += 1
    temp //= 10

print("Цифр a:", count_a)
print("Сумма цифр >a:", sum_gt_a)
print("Сумма четных цифр:", sum_even)
print("Цифр x и y:", count_xy)