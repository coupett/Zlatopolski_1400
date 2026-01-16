n = int(input())
temp = n

# а) количество цифр 3
count3 = 0
# б) сколько раз встречается последняя цифра
last_digit = n % 10
count_last = 0
# в) количество четных цифр
count_even = 0
# г) сумма цифр > 5
sum_gt5 = 0
# д) произведение цифр > 7
prod_gt7 = 1
has_gt7 = False
# е) сколько раз встречаются цифры 0 и 5
count_0_5 = 0

while temp > 0:
    digit = temp % 10
    if digit == 3:
        count3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_gt5 += digit
    if digit > 7:
        prod_gt7 *= digit
        has_gt7 = True
    if digit == 0 or digit == 5:
        count_0_5 += 1
    temp //= 10

if not has_gt7:
    prod_gt7 = 0

print("Цифр 3:", count3)
print("Последняя цифра встречается:", count_last)
print("Четных цифр:", count_even)
print("Сумма цифр >5:", sum_gt5)
print("Произведение цифр >7:", prod_gt7)
print("Цифр 0 и 5:", count_0_5)