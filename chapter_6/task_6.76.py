a = int(input())
b = int(input())

length = 0
x, y = 1, 1
direction = 0
while x <= a and y <= b:
    if direction == 0:
        length += (a - x)
        x = a
        direction = 1
    elif direction == 1:
        length += (b - y)
        y = b
        direction = 2
    elif direction == 2:
        length += (x - 1)
        x = 1
        direction = 3
    else:
        length += (y - 2)
        y = 2
        direction = 0

print("Длина ограждения:", length)