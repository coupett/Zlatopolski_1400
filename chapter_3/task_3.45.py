k = int(input())
n = (k + 1) // 2
chislo = n + 9
if k % 2 == 1:
    cifra = chislo // 10
else:
    cifra = chislo % 10
print(n)
print(chislo)
print(cifra)