import math
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
if a**2 + 25 == 0:
    print("Ошибка: знаменатель a^2 + 25 не может быть равен 0")
elif b + (a + b)/2 < 0:
    print("Ошибка: выражение под корнем должно быть неотрицательным")
else:
    n_x = (2 / (a**2 + 25)) + b
    d_x = math.sqrt(b + (a + b) / 2)
    x = n_x / d_x
    print(f"x = {x}")
if a == 0:
    print("Ошибка: a не может быть равен 0 (деление на ноль)")
else:
    y = (abs(a) + 2 * math.sin(b)) / (5.5 * a)
    print(f"y = {y}")