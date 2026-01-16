a = 425
b = 131
results = []

while a > 0 and b > 0:
    if a >= b:
        count = a // b
        if count > 0:
            results.append((b, count))
        a = a % b
    else:
        count = b // a
        if count > 0:
            results.append((a, count))
        b = b % a

print("Квадраты:")
for size, count in results:
    print(f"{size}x{size}: {count} шт.")