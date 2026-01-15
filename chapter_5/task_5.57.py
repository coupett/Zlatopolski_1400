area = 0
step = 0.001
x = 0
while x <= 10:  # примерный диапазон
    y = 0.3 * (x - 1)**2 + 3
    if 2 <= y <= 4:
        area += step
    x += step
print(area)