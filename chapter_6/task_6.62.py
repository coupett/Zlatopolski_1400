n = int(input())
# a) число справа налево
temp = n
reverse_num = 0
while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp //= 10
print("а)", reverse_num)

# б) с двойками в начале и конце
print("б)", int("2" + str(n) + "2"))

# в) удаление цифры a
n_copy = n
a = int(input())
result = 0
multiplier = 1
while n_copy > 0:
    digit = n_copy % 10
    if digit != a:
        result = digit * multiplier + result
        multiplier *= 10
    n_copy //= 10
print("в)", result)

# г) перестановка первой и последней
temp = n
digits = []
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

if digits:
    first = digits[-1]
    last = digits[0]
    digits[-1] = last
    digits[0] = first

    result = 0
    for digit in digits[::-1]:
        result = result * 10 + digit
    print("г)", result)

# д) приписывание такого же числа
print("д)", int(str(n) + str(n)))