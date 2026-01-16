n = int(input())
digits = []
temp = n
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

min_digit = min(digits)
max_digit = max(digits)

for i in range(len(digits)):
    if digits[i] == min_digit:
        min_from_end = i + 1
    if digits[i] == max_digit:
        max_from_end = i + 1

digits_rev = digits[::-1]
for i in range(len(digits_rev)):
    if digits_rev[i] == min_digit:
        min_from_start = i + 1
    if digits_rev[i] == max_digit:
        max_from_start = i + 1

print("а)", max_from_end, min_from_end)
print("б)", max_from_start, min_from_start)