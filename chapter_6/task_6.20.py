n = int(input())
sum_d = 0
count = 0
prod = 1
first_digit = 0
last_digit = n % 10

while n > 0:
    digit = n % 10
    sum_d += digit
    count += 1
    prod *= digit
    n //= 10
    if n == 0:
        first_digit = digit

print("Сумма цифр:", sum_d)
print("Количество цифр:", count)
print("Произведение цифр:", prod)
print("Среднее арифметическое:", sum_d / count)
print("Сумма квадратов:", sum(i*i for i in map(int, str(abs(n)))))
print("Сумма кубов:", sum(i**3 for i in map(int, str(abs(n)))))
print("Первая цифра:", first_digit)
print("Сумма первой и последней цифр:", first_digit + last_digit)