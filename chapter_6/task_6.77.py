n = int(input())
temp = n
digits = []

while temp > 0:
    digits.append(temp % 10)
    temp //= 10

# а) все цифры одинаковы
all_same = all(d == digits[0] for d in digits)
print("а)", all_same)

# б) две одинаковые цифры рядом
has_pair = False
for i in range(len(digits) - 1):
    if digits[i] == digits[i + 1]:
        has_pair = True
        break
print("б)", has_pair)