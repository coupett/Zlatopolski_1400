n = int(input())
a = list(map(int, input().split()))

# a) сумма модулей
sum_abs = 0
for num in a:
    sum_abs += abs(num)
print("а)", sum_abs)

# б) произведение модулей
product_abs = 1
for num in a:
    product_abs *= abs(num)
print("б)", product_abs)

# в) суммы соседних элементов
sums = []
for i in range(n-1):
    sums.append(a[i] + a[i+1])
print("в)", sums)

# г) знакопеременная сумма
alt_sum = 0
sign = 1
for num in a:
    alt_sum += sign * num
    sign = -sign
print("г)", alt_sum)