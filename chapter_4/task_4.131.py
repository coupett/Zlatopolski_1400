# Первая тройка
a1 = float(input())
b1 = float(input())
c1 = float(input())
# Среднее в первой тройке
if (b1 < a1 < c1) or (c1 < a1 < b1):
    sred1 = a1
elif (a1 < b1 < c1) or (c1 < b1 < a1):
    sred1 = b1
else:
    sred1 = c1

# Вторая тройка
a2 = float(input())
b2 = float(input())
c2 = float(input())
# Среднее во второй тройке
if (b2 < a2 < c2) or (c2 < a2 < b2):
    sred2 = a2
elif (a2 < b2 < c2) or (c2 < b2 < a2):
    sred2 = b2
else:
    sred2 = c2

sred_arif = (sred1 + sred2) / 2
print(sred_arif)