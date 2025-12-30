k = int(input())
if k <= 102:
    if k % 2 == 1:
        num = 50 + (k - 1) // 2
        cifra = num // 10
    else:
        num = 50 + (k - 2) // 2
        cifra = num % 10
else:
    k -= 102
    if k % 3 == 1:
        num = 100 + (k - 1) // 3
        cifra = num // 100
    elif k % 3 == 2:
        num = 100 + (k - 2) // 3
        cifra = (num // 10) % 10
    else:
        num = 100 + (k - 3) // 3
        cifra = num % 10
print(cifra)