price_per_kg = float(input())
for weight in range(100, 2100, 100):
    cost = (weight / 1000) * price_per_kg
    print(weight, cost)