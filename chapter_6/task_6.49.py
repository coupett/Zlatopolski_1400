n = int(input())
temp = n
digits = []
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

sum_digits = sum(digits)
product = 1
for d in digits:
    product *= d
count = len(digits)

print("а)", sum_digits > 10)
print("б)", product < 50)
print("в)", count % 2 == 0)
print("г)", 1000 <= n <= 9999)

if digits:
    first_digit = digits[-1]
    print("д)", first_digit <= 6)
    last_digit = digits[0]
    print("е)", first_digit == last_digit)
    print("ж)", "первая" if first_digit > last_digit else "последняя" if last_digit > first_digit else "равны")