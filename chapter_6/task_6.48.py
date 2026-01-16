n = int(input())
temp = n
max_odd = -1
digits = []
while temp > 0:
    digit = temp % 10
    digits.append(digit)
    if digit % 2 == 1:
        if digit > max_odd:
            max_odd = digit
    temp //= 10

digits = digits[::-1]
min_digit = min(digits)
for i in range(len(digits)):
    if digits[i] == min_digit:
        min_index = i + 1
        break

if max_odd != -1:
    print("а)", max_odd)
else:
    print("а) нечетных цифр нет")
print("б)", min_index)