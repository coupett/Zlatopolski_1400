import math
e = float(input("Введите значение e: "))
f = float(input("Введите значение f: "))
g = float(input("Введите значение g: "))
h = float(input("Введите значение h: "))
if f == 0:
    print("Ошибка: f не может быть равен 0 (деление на ноль)")
elif e - 3/f < 0:
    print("Ошибка: выражение под корнем должно быть неотрицательным")
else:
    a_result = (math.sqrt(e - 3/f))**3 + g
    print(f"a = {a_result}")
b_result = math.sin(e) + (math.cos(h))**2
print(f"b = {b_result}")
if e * f - 3 == 0:
    print("Ошибка: знаменатель e*f - 3 не может быть равен 0")
else:
    c_result = (33 * g) / (e * f - 3)
    print(f"c = {c_result}")