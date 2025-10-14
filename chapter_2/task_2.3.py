import math
print("Пункт а)")
a = int(input("Введите число: "))
b = 2 * a + math.sin(abs(3*a))
c = 3.56
x = math.sqrt(b/c)
print(x)

print("Пункт б)")
x = int(input("Введите число: "))
y = math.sin(3.2 + (1 + x)**1/2/(abs(5 * x)))
print(y)