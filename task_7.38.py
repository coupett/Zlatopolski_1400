people = []
densities = []
for _ in range(12):
    p, d = map(float, input().split())
    people.append(p)
    densities.append(d)

total_area = 0
for i in range(12):
    total_area += people[i] / densities[i]

print("Общая площадь:", total_area)