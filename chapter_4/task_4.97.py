k = int(input())
if k <= 9:
    cifra = k
elif k <= 189:
    m = k - 9
    if m % 2 == 1:
        num = 10 + (m - 1) // 2
        cifra = num // 10
    else:
        num = 10 + (m - 2) // 2
        cifra = num % 10
else:
    m = k - 189
    if m % 3 == 1:
        num = 100 + (m - 1) // 3
        cifra = num // 100
    elif m % 3 == 2:
        num = 100 + (m - 2) // 3
        cifra = (num // 10) % 10
    else:
        num = 100 + (m - 3) // 3
        cifra = num % 10
print(cifra)