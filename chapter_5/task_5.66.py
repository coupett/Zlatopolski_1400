total = 0
for n in range(1, 13):
    s = 0
    for i in range(1, 2*n, 2):
        s += i
    total += s
print(total)