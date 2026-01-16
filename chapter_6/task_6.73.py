m = int(input())
g = int(input())
z = int(input())

if z == 0 or g == 0:
    if m == g:
        print("является")
    else:
        print("не является")
else:
    temp = m
    while temp > g and temp % g == 0:
        temp //= g

    if temp == 1 and m >= g:
        print("является")
    else:
        print("не является")