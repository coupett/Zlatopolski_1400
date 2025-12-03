h = int(input())
m = int(input())
for t in range(0, 721):
    delta = 30 * h - 5.5 * m - 5.5 * t
    delta_mod = delta % 360
    if delta_mod == 0:
        print(t)
        break

h = int(input())
m = int(input())
for t in range(0, 721):
    delta = 30 * h - 5.5 * m - 5.5 * t
    delta_mod = delta % 360
    if delta_mod == 90 or delta_mod == 270:
        print(t)
        break