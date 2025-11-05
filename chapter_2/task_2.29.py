x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())

a = ((x2-x1)**2 + (y2-y1)**2)**0.5
b = ((x3-x2)**2 + (y3-y2)**2)**0.5
c = ((x1-x3)**2 + (y1-y3)**2)**0.5

perimeter = a + b + c
p = perimeter / 2
area = (p * (p-a) * (p-b) * (p-c))**0.5

print(perimeter)
print(area)