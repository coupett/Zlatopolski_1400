x = 2
s = 0
power = x
for i in range(1, 12, 2):
    s += power / i
    power *= x * x
print(s)