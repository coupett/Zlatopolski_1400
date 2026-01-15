n = int(input())
v = [0] * (n + 1)
v[1] = 0
v[2] = 0
v[3] = 1.5
for i in range(4, n + 1):
    v[i] = (i - 1) / (i * i + 1) * v[i-1] - v[i-2] + v[i-3]
print(v[n])