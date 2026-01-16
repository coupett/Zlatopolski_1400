n = int(input())
a, b = 0, 1

while a < n:
    a, b = b, a + b

if a == n or n == 0:
    print("является")
else:
    print("не является")