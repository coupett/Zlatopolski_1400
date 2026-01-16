n = int(input())
a = int(input())
b = int(input())
k = int(input())
m = int(input())

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

print("а)", sum_digits < a)
print("б)", product > b)

is_k_digit = False
if k == 1 and 0 <= n <= 9:
    is_k_digit = True
elif k == 2 and 10 <= n <= 99:
    is_k_digit = True
elif k == 3 and 100 <= n <= 999:
    is_k_digit = True
elif k == 4 and 1000 <= n <= 9999:
    is_k_digit = True
elif k == 5 and 10000 <= n <= 99999:
    is_k_digit = True
elif k == 6 and 100000 <= n <= 999999:
    is_k_digit = True
elif k > 6 and 10**(k-1) <= n <= 10**k - 1:
    is_k_digit = True
print("в)", is_k_digit)

print("г)", first_digit > m)