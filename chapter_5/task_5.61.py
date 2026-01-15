x = int(input())
y = int(input())

# Способ 1
res = 0
for _ in range(y):
    res += x
print(res)

# Способ 2
res = 0
if x < y:
    for _ in range(x):
        res += y
else:
    for _ in range(y):
        res += x
print(res)