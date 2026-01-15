n = int(input())

# а) все делители
print("Делители:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
print()

# б) сумма делителей
sum_div = 0
for i in range(1, n+1):
    if n % i == 0:
        sum_div += i
print("Сумма делителей:", sum_div)

# в) сумма четных делителей
sum_even = 0
for i in range(2, n+1, 2):
    if n % i == 0:
        sum_even += i
print("Сумма четных делителей:", sum_even)

# г) количество делителей
count_div = 0
for i in range(1, n+1):
    if n % i == 0:
        count_div += 1
print("Количество делителей:", count_div)

# д) количество нечетных делителей
count_odd = 0
for i in range(1, n+1, 2):
    if n % i == 0:
        count_odd += 1
print("Количество нечетных делителей:", count_odd)

# е) количество делителей и четных
count_even = 0
for i in range(2, n+1, 2):
    if n % i == 0:
        count_even += 1
print("Четных делителей:", count_even)

# ж) количество делителей > d
d = int(input())
count_greater = 0
for i in range(d+1, n+1):
    if n % i == 0:
        count_greater += 1
print("Делителей больше", d, ":", count_greater)