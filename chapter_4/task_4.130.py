a = float(input())
b = float(input())
c = float(input())
maximal = a
if b > maximal:
    maximal = b
if c > maximal:
    maximal = c
proizv = a * b * c / maximal
print(proizv)