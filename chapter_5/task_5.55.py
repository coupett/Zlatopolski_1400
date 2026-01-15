s = 0
for i in range(1, 11):
    s += i * i * (1 if i % 2 == 0 else -1)
print(s)