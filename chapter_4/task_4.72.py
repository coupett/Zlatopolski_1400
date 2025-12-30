x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())
x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())
inside12 = x1 >= x2 and y1 >= y2 and x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2
inside21 = x2 >= x1 and y2 >= y1 and x2 + w2 <= x1 + w1 and y2 + h2 <= y1 + h1
intersect = not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)
if inside12:
    print("принадлежат")
else:
    print("не принадлежат")
if inside12 or inside21:
    print("да")
else:
    print("нет")
if intersect:
    print("пересекаются")
else:
    print("не пересекаются")