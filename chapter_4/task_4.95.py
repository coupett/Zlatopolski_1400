n = int(input())
if n == 1:
    cifra = 0
else:
    m = n - 1
    if m <= 9:
        cifra = m
    else:
        m -= 9
        num = 10 + (m - 1) // 2
        if m % 2 == 1:
            cifra = num // 10
        else:
            cifra = num % 10
print(cifra)