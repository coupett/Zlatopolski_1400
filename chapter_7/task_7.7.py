resistances = list(map(float, input().split()))
total = 0
for r in resistances:
    total += 1/r
print(1/total)