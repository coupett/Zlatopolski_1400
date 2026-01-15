# а) пробег за 2-10 дни
probeg = 10
for day in range(2, 11):
    probeg *= 1.1
    print(day, probeg)

# б) суммарный путь за 7 дней
total = 10
prob = 10
for day in range(2, 8):
    prob *= 1.1
    total += prob
print(total)