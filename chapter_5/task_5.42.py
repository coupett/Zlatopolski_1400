# a) расстояние от дома после 100 этапа
n = 100
dist = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        dist += 1 / i
    else:
        dist -= 1 / i
print(dist)

# б) общий пройденный путь
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total)