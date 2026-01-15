# а) прирост за первые 10 месяцев
vklad = 1000
for month in range(1, 11):
    prirast = vklad * 0.02
    vklad += prirast
    print(month, prirast)

# б) сумма через 3-12 месяцев
vklad = 1000
for month in range(1, 13):
    vklad *= 1.02
    if month >= 3:
        print(month, vklad)