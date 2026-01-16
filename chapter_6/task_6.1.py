a = int(input())
b = int(input())

# a) целочисленное деление
cel = 0
temp = a
while temp >= b:
    temp -= b
    cel += 1
print(cel)

# б) остаток от деления
ost = a
while ost >= b:
    ost -= b
print(ost)