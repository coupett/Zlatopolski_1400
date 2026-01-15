# а)
for num in range(10, 100):
    d1 = num // 10
    d2 = num % 10
    if (d1*d1 + d2*d2) % 13 == 0:
        print(num)

# б)
for num in range(10, 100):
    d1 = num // 10
    d2 = num % 10
    s = d1 + d2
    if s + s*s == num:
        print(num)