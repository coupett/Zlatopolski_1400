x = 2
s = 1
power = 1
sign = -1
for i in range(2, 12):
    power *= x
    s += sign * (i / (i + 1)) * power
    sign = -sign
print(s)