k = int(input())
if k % 2 == 1:
    num = 10 + (k - 1) // 2
    cifra = num // 10
else:
    num = 10 + (k - 2) // 2
    cifra = num % 10
print(cifra)