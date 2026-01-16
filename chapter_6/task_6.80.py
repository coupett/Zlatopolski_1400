n = int(input())
temp = n
digits = []

while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]
is_ordered = True
for i in range(len(digits) - 1):
    if digits[i] >= digits[i + 1]:
        is_ordered = False
        break

print(is_ordered)