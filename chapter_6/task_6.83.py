n = int(input())
temp = n
digits = []

while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]
is_monotonic = True

# Проверка возрастания
is_increasing = True
for i in range(len(digits) - 1):
    if digits[i] >= digits[i + 1]:
        is_increasing = False
        break

# Проверка убывания
is_decreasing = True
for i in range(len(digits) - 1):
    if digits[i] <= digits[i + 1]:
        is_decreasing = False
        break

print(is_increasing or is_decreasing)