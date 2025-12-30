n = int(input())
y = n // 12
m = n % 12
if y % 10 == 1 and y % 100 != 11:
    slovo_y = "год"
elif 2 <= y % 10 <= 4 and not (10 <= y % 100 <= 20):
    slovo_y = "года"
else:
    slovo_y = "лет"
if m == 0:
    print(y, slovo_y, "ровно")
elif m == 1:
    slovo_m = "месяц"
elif 2 <= m <= 4:
    slovo_m = "месяца"
else:
    slovo_m = "месяцев"
print(y, slovo_y, m, slovo_m)