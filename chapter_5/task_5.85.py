a = int(input())
b = int(input())
s = 0
for i in range(a, b+1):
    if i > 0 and i % 4 == 0:
        s += i
print(s)