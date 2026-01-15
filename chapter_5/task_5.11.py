import math
R = 6350
for h in range(1, 11):
    d = math.sqrt((R + h) ** 2 - R ** 2)
    print(h, d)