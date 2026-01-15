n = int(input())
a = [0] * (n + 1)
a[0] = 1
for k in range(1, n + 1):
    a[k] = k * a[k-1] + 1/k
for i in range(n + 1):
    print(a[i])