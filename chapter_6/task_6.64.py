n = int(input())
denominations = [64, 32, 16, 8, 4, 2, 1]
counts = [0] * 7

temp = n
for i in range(7):
    counts[i] = temp // denominations[i]
    temp = temp % denominations[i]

print("Купюры:")
for i in range(7):
    if counts[i] > 0:
        print(f"{denominations[i]} руб.: {counts[i]} шт.")