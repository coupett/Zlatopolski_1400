n = int(input())
temp = n
digits = set()

while temp > 0:
    digits.add(temp % 10)
    temp //= 10

sorted_digits = sorted(digits)
if len(sorted_digits) >= 2:
    print("а)", sorted_digits[-1], sorted_digits[-2])
    print("б)", sorted_digits[0], sorted_digits[1])
else:
    print("мало различных цифр")