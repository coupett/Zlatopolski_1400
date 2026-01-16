n = int(input())
digits = []
temp = n
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]
min_digit = min(digits)
max_digit = max(digits)

min_index = digits.index(min_digit)
max_index = digits.index(max_digit)

if min_index < max_index:
    print("левее минимальная")
else:
    print("левее максимальная")