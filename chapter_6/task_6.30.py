a = int(input())
b = int(input())
cel = 0
temp = b
while temp >= a:
    temp -= a
    cel += 1
print(cel)