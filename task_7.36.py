areas = []
yields = []
for _ in range(10):
    area, yield_val = map(float, input().split())
    areas.append(area)
    yields.append(yield_val)

total_wheat = 0
for i in range(10):
    total_wheat += areas[i] * yields[i]

avg_yield = total_wheat / sum(areas)
print("Общий сбор:", total_wheat)
print("Средняя урожайность:", avg_yield)