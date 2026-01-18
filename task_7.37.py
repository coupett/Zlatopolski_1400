people = []
areas = []
for _ in range(12):
    p, a = map(float, input().split())
    people.append(p)
    areas.append(a)

total_people = sum(people)
total_area = sum(areas)
density = total_people / total_area
print("Средняя плотность:", density)