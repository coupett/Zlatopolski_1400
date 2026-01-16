n = int(input())
digits = []
temp = n
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
for digit in reversed(digits):
    print(digit)