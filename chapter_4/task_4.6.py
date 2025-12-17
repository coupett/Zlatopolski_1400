x = float(input())
if x < 0:
    y = 1
elif x <= 2:
    y = 1 + 0.5 * x
else:
    y = 2
print(y)

x = float(input())
if x < 0:
    y = -3
elif x <= 3:
    y = x - 3
else:
    y = 0
print(y)