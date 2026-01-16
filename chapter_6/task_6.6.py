fact = int(input())
n = 1
res = 1
while res < fact:
    n += 1
    res *= n
if res == fact:
    print(n)
else:
    print("Не факториал")