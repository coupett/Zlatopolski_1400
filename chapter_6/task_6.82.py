n = int(input())
temp = n
digits = []

while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]
is_non_decreasing = True
for i in range(len(digits) - 1):
    if digits[i] > digits[i + 1]:
        is_non_decreasing = False
        break

print(is_non_decreasing)