# а) урожайность за 2-8 годы
urozh = 20
for year in range(2, 9):
    urozh *= 1.02
    print(year, urozh)

# б) площадь за 4-7 годы
plosh = 100
for year in range(2, 8):
    plosh *= 1.05
    if year >= 4:
        print(year, plosh)

# в) урожай за 6 лет
plosh = 100
urozh = 20
total = 0
for year in range(1, 7):
    total += plosh * urozh
    plosh *= 1.05
    urozh *= 1.02
print(total)