n = int(input())
x = (n + 1) % 12
if x == 0:
    x = 12
print(x)