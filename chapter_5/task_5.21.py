price_per_kg = float(input())
for weight in range(50, 1050, 50):
    cost = (weight / 1000) * price_per_kg
    print(weight, cost)