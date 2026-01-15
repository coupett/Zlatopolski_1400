area = 0
step = 0.001
x = -2
while x <= 0:
    y = 0.4 * (x + 2)**2 + 1
    if 0 <= y <= 2:
        area += step * y
    x += step
print(area)