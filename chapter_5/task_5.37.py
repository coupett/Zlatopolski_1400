n = int(input())
s = 0
sign = 1
for i in range(1, n + 1):
    s += sign / i
    sign = -sign
print(s)