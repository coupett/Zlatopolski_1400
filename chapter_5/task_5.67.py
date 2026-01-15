n = int(input())
s = 0
first = n * n - n + 1
for i in range(n):
    s += first + 2*i
print(s)