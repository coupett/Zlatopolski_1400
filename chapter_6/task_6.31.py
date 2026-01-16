# a) месяц, когда прирост превысит 30 руб.
vklad = 1000
month = 1
while True:
    prirast = vklad * 0.02
    if prirast > 30:
        print("Месяц:", month)
        break
    vklad += prirast
    month += 1

# б) месяц, когда вклад превысит 1200 руб.
vklad = 1000
month = 1
while vklad <= 1200:
    vklad *= 1.02
    month += 1
print("Месяц:", month)