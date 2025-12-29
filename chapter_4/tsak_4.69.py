a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
sizes = [(c, d), (c, e), (d, c), (d, e), (e, c), (e, d)]
max_count = 0
for x, y in sizes:
    count1 = (a // x) * (b // y)
    count2 = (a // y) * (b // x)
    max_count = max(max_count, count1, count2)
print(max_count)