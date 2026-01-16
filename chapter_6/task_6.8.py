# Вариант 1
n = int(input())
i = 1
while i*i <= n:
    i += 1
print(i)

# Вариант 2
n = int(input())
for i in range(1, 101):
    if i*i > n:
        print(i)
        break