n = int(input())
temp = n
max_digit = 0
max_pos_end = 0
max_pos_start = 0
min_digit = 9
min_pos_end = 0
min_pos_start = 0
pos = 0
digits = []

while temp > 0:
    digit = temp % 10
    digits.append(digit)
    pos += 1
    if digit > max_digit:
        max_digit = digit
        max_pos_end = pos
    if digit < min_digit:
        min_digit = digit
        min_pos_end = pos
    temp //= 10

# Определяем позиции от начала числа
digits_rev = list(reversed(digits))
for i in range(len(digits_rev)):
    if digits_rev[i] == max_digit:
        max_pos_start = i + 1
    if digits_rev[i] == min_digit:
        min_pos_start = i + 1

print("Максимальная цифра:")
print("От конца:", max_pos_end)
print("От начала:", max_pos_start)
print("Минимальная цифра:")
print("От конца:", min_pos_end)
print("От начала:", min_pos_start)