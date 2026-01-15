m = int(input())
k = int(input())

# Определяем масть
if m == 1:
    mast = "пик"
elif m == 2:
    mast = "треф"
elif m == 3:
    mast = "бубен"
elif m == 4:
    mast = "червей"
else:
    mast = "неизвестная масть"

# Определяем достоинство
if k == 6:
    dost = "Шестерка"
elif k == 7:
    dost = "Семерка"
elif k == 8:
    dost = "Восьмерка"
elif k == 9:
    dost = "Девятка"
elif k == 10:
    dost = "Десятка"
elif k == 11:
    dost = "Валет"
elif k == 12:
    dost = "Дама"
elif k == 13:
    dost = "Король"
elif k == 14:
    dost = "Туз"
else:
    dost = "Неизвестная карта"

print(dost, mast)