n = int(input())
k = int(input())
b = int(input())
x = int(input())
y = int(input())
a = int(input())
b2 = int(input())
m = int(input())
n2 = int(input())

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

if digits:
    first_digit = digits[-1]
    last_digit = digits[0]

print("а)", sum_digits > k and n % 2 == 0)
print("б)", count % 2 == 0 and n <= b)
print("г)", first_digit == x and last_digit == y)
print("д)", product < a and n % b2 == 0)
print("е)", sum_digits > m and n % n2 == 0)