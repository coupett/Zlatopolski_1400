import math
e = float(input("Введите значение e: "))
f = float(input("Введите значение f: "))
g = float(input("Введите значение g: "))
h = float(input("Введите значение h: "))
a_result = (e + f/2) / 3
print(f"a = {a_result}")
b_result = abs(h**2 - g)
print(f"b = {b_result}")
if (g - h)**2 - 3 * math.sin(e) < 0:
    print("Ошибка: выражение под корнем должно быть неотрицательным")
else:
    c_result = math.sqrt((g - h)**2 - 3 * math.sin(e))
    print(f"c = {c_result}")