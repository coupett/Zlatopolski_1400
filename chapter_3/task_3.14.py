k = int(input())
podezd = (k - 1) // 54 + 1
etazh = ((k - 1) % 54) // 6 + 1
nomer_na_etazhe = ((k - 1) % 54) % 6 + 1
print(podezd)
print(etazh)
print(nomer_na_etazhe)