num = int(input())
k = int(input())
s = 0
p = 1
for i in range(k):
    digit = num % 10
    s += digit
    p *= digit
    num //= 10
print(p, s)